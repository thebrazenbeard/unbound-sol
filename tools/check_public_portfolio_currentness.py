#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_CENSUS = ROOT / "research" / "OWNED_PORTFOLIO_MECHANISM_CENSUS_20260923_V1.json"
API_ROOT = "https://api.github.com"


def _api_json(path: str, token: str | None) -> dict:
    request = urllib.request.Request(
        f"{API_ROOT}{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "unbound-sol-public-currentness",
        },
    )
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def _repo_path(repository: str) -> tuple[str, str]:
    owner, sep, name = repository.partition("/")
    if not sep or not owner or not name or "/" in name:
        raise ValueError(f"invalid repository_full_name: {repository!r}")
    return urllib.parse.quote(owner, safe=""), urllib.parse.quote(name, safe="")


def inspect_subject(subject: dict, token: str | None) -> dict:
    repository = subject["repo"]
    owner, name = _repo_path(repository)
    expected = {
        "visibility": subject["visibility"],
        "archived": subject["archived"],
        "default_branch": subject["default_branch"],
        "head": subject["ref"],
    }

    meta = _api_json(f"/repos/{owner}/{name}", token)
    default_branch = meta.get("default_branch")
    current = {
        "visibility": meta.get("visibility"),
        "archived": meta.get("archived"),
        "default_branch": default_branch,
        "head": None,
    }

    if default_branch:
        branch_name = urllib.parse.quote(default_branch, safe="")
        ref = _api_json(f"/repos/{owner}/{name}/git/ref/heads/{branch_name}", token)
        current["head"] = ref.get("object", {}).get("sha")

    drift = [
        key
        for key in ("visibility", "archived", "default_branch", "head")
        if current.get(key) != expected.get(key)
    ]

    volatile = subject.get("head_volatility") == "ACTIVE_UPSTREAM"
    volatile_head_only = volatile and drift == ["head"]

    return {
        "repo": repository,
        "ref_role": subject.get("ref_role"),
        "expected": expected,
        "current": current,
        "status": (
            "DRIFTED_VOLATILE"
            if volatile_head_only
            else ("DRIFTED" if drift else "CURRENT")
        ),
        "drift_fields": drift,
        "head_volatility": subject.get("head_volatility"),
        "latest_live_head_observed": subject.get("latest_live_head_observed"),
    }


def run(census_path: pathlib.Path, token: str | None) -> tuple[dict, int]:
    census = json.loads(census_path.read_text(encoding="utf-8"))
    subjects = census.get("public_repositories", [])

    results: list[dict] = []
    unknown: list[dict] = []

    for subject in subjects:
        try:
            results.append(inspect_subject(subject, token))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, KeyError, json.JSONDecodeError) as exc:
            unknown.append(
                {
                    "repo": subject.get("repo"),
                    "status": "UNKNOWN",
                    "error_class": type(exc).__name__,
                    "error": str(exc),
                }
            )

    drifted = [item for item in results if item["status"] in {"DRIFTED", "DRIFTED_VOLATILE"}]
    volatile_drifted = [item for item in results if item["status"] == "DRIFTED_VOLATILE"]
    unexpected_drifted = [item for item in results if item["status"] == "DRIFTED"]

    if unexpected_drifted:
        status = "DRIFTED"
        exit_code = 1
    elif volatile_drifted:
        status = "DRIFTED_VOLATILE"
        exit_code = 1
    elif unknown:
        status = "UNKNOWN"
        exit_code = 2
    else:
        status = "CURRENT"
        exit_code = 0

    report = {
        "schema": "UNBOUND_SOL_PUBLIC_PORTFOLIO_CURRENTNESS_CHECK_V1",
        "status": status,
        "census": str(census_path.relative_to(ROOT) if census_path.is_relative_to(ROOT) else census_path),
        "observed_date": census.get("observed_date"),
        "checked_subjects": len(subjects),
        "current_count": sum(1 for item in results if item["status"] == "CURRENT"),
        "drifted_count": len(drifted),
        "volatile_drifted_count": len(volatile_drifted),
        "unexpected_drifted_count": len(unexpected_drifted),
        "unknown_count": len(unknown),
        "results": results,
        "unknown": unknown,
        "claim_ceiling": (
            "Read-only live comparison of stored public repository metadata/default-head bindings. "
            "It does not refresh the census, validate private repositories, re-admit mechanisms, "
            "or authorize any effect."
        ),
    }
    return report, exit_code


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read-only live currentness check for the public owned-portfolio census."
    )
    parser.add_argument(
        "--census",
        type=pathlib.Path,
        default=DEFAULT_CENSUS,
        help="Path to the machine-readable portfolio census.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the complete machine-readable report.",
    )
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    report, exit_code = run(args.census.resolve(), token)

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(
            f"portfolio currentness: {report['status']} "
            f"(current={report['current_count']} "
            f"drifted={report['drifted_count']} unknown={report['unknown_count']})"
        )
        for item in report["results"]:
            if item["status"] in {"DRIFTED", "DRIFTED_VOLATILE"}:
                print(
                    f"{item['status']} {item['repo']}: "
                    + ", ".join(item["drift_fields"])
                )
        for item in report["unknown"]:
            print(f"UNKNOWN {item['repo']}: {item['error_class']}: {item['error']}")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
