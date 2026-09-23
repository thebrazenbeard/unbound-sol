#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import tempfile

from validate_behavior_training_pairs import (
    DEFAULT_PAIRS,
    DEFAULT_TARGETS,
    EXPOSURE,
    load_active_targets,
    load_pairs,
    validate,
)

ROOT = pathlib.Path(__file__).resolve().parents[1]
FORMAT_SCHEMAS = {
    "preference": "UNBOUND_SOL_EXPORTED_PREFERENCE_V1",
    "sft": "UNBOUND_SOL_EXPORTED_SFT_V1",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_line(value: dict) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def export_record(pair: dict, output_format: str) -> dict:
    metadata = {
        "source_id": pair["id"],
        "targets": pair["targets"],
        "case_class": pair["case_class"],
        "exposure_class": pair["exposure_class"],
        "holdout_eligible": pair["holdout_eligible"],
        "failure_mode": pair["failure_mode"],
        "why_preferred": pair["why_preferred"],
    }

    if output_format == "preference":
        return {
            "schema": FORMAT_SCHEMAS[output_format],
            "id": pair["id"],
            "prompt": pair["prompt"],
            "chosen": pair["preferred"],
            "rejected": pair["rejected"],
            "metadata": metadata,
        }

    if output_format == "sft":
        return {
            "schema": FORMAT_SCHEMAS[output_format],
            "id": pair["id"],
            "messages": [
                {"role": "user", "content": pair["prompt"]},
                {"role": "assistant", "content": pair["preferred"]},
            ],
            "metadata": metadata,
        }

    raise ValueError(f"unsupported output format: {output_format}")


def atomic_write(path: pathlib.Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="wb",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    ) as handle:
        temp_path = pathlib.Path(handle.name)
        handle.write(data)
        handle.flush()
    temp_path.replace(path)


def export(
    pairs_path: pathlib.Path,
    targets_path: pathlib.Path,
    output_path: pathlib.Path,
    manifest_path: pathlib.Path,
    output_format: str,
) -> dict:
    pairs_path = pairs_path.resolve()
    targets_path = targets_path.resolve()
    output_path = output_path.resolve()
    manifest_path = manifest_path.resolve()

    if output_path == pairs_path:
        raise ValueError("refusing to overwrite source training corpus")
    if manifest_path in {pairs_path, output_path}:
        raise ValueError("manifest path must be distinct from source and output")

    active_targets = load_active_targets(targets_path)
    pairs = load_pairs(pairs_path)
    validation = validate(pairs, active_targets)

    if validation["exposure_class"] != EXPOSURE:
        raise ValueError("source corpus is not public training/regression material")
    if validation["holdout_eligible"] is not False:
        raise ValueError("source corpus must be holdout-ineligible")

    exported = [export_record(pair, output_format) for pair in pairs]
    output_text = "".join(canonical_line(item) + "\n" for item in exported)
    output_bytes = output_text.encode("utf-8")
    source_bytes = pairs_path.read_bytes()

    manifest = {
        "schema": "UNBOUND_SOL_BEHAVIOR_TRAINING_EXPORT_MANIFEST_V1",
        "format": output_format,
        "record_schema": FORMAT_SCHEMAS[output_format],
        "example_count": len(exported),
        "source": {
            "path": str(pairs_path.relative_to(ROOT) if pairs_path.is_relative_to(ROOT) else pairs_path),
            "sha256": sha256_bytes(source_bytes),
            "schema": "UNBOUND_SOL_BEHAVIOR_PREFERENCE_PAIR_V1",
            "exposure_class": EXPOSURE,
            "holdout_eligible": False,
        },
        "output": {
            "path": str(output_path),
            "sha256": sha256_bytes(output_bytes),
            "exposure_class": "DERIVED_PUBLIC_TRAINING_REGRESSION_ONLY",
            "holdout_eligible": False,
        },
        "claim_ceiling": (
            "This manifest binds a deterministic format conversion of already-exposed "
            "public training data. It does not establish training, transfer, model quality, "
            "or holdout eligibility."
        ),
    }

    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")
    atomic_write(output_path, output_bytes)
    atomic_write(manifest_path, manifest_bytes)

    if sha256_bytes(output_path.read_bytes()) != manifest["output"]["sha256"]:
        raise RuntimeError("output readback digest mismatch")
    if json.loads(manifest_path.read_text(encoding="utf-8")) != manifest:
        raise RuntimeError("manifest readback mismatch")

    return manifest


def self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="unbound-sol-training-export-") as td:
        root = pathlib.Path(td)
        manifests = []
        for output_format in sorted(FORMAT_SCHEMAS):
            output = root / f"{output_format}.jsonl"
            manifest = root / f"{output_format}.manifest.json"
            result = export(
                DEFAULT_PAIRS,
                DEFAULT_TARGETS,
                output,
                manifest,
                output_format,
            )
            if result["example_count"] < 1:
                raise RuntimeError("self-test exported no records")
            lines = [json.loads(line) for line in output.read_text(encoding="utf-8").splitlines() if line]
            if len(lines) != result["example_count"]:
                raise RuntimeError("self-test output line count mismatch")
            if any(item["metadata"]["holdout_eligible"] is not False for item in lines):
                raise RuntimeError("self-test export created holdout-eligible data")
            if any(item["metadata"]["exposure_class"] != EXPOSURE for item in lines):
                raise RuntimeError("self-test export lost source exposure class")
            manifests.append(result)

        if manifests[0]["source"]["sha256"] != manifests[1]["source"]["sha256"]:
            raise RuntimeError("formats disagree on source digest")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministically export public Behavior V3 training pairs."
    )
    parser.add_argument("--pairs", type=pathlib.Path, default=DEFAULT_PAIRS)
    parser.add_argument("--targets", type=pathlib.Path, default=DEFAULT_TARGETS)
    parser.add_argument("--format", choices=sorted(FORMAT_SCHEMAS))
    parser.add_argument("--output", type=pathlib.Path)
    parser.add_argument("--manifest", type=pathlib.Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("behavior training exporter self-test: PASS")
        return 0

    if args.format is None or args.output is None:
        parser.error("--format and --output are required unless --self-test is used")

    manifest_path = args.manifest or pathlib.Path(str(args.output) + ".manifest.json")
    result = export(
        args.pairs,
        args.targets,
        args.output,
        manifest_path,
        args.format,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
