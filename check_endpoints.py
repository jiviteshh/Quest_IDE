"""Local QuestIDE API smoke test.

Run from the repository root:
    python check_endpoints.py

The script checks every endpoint currently used by the frontend and never prints
API keys or response bodies beyond a short sanitized preview.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BACKEND_URL = os.getenv("QUESTIDE_BACKEND_URL", "http://localhost:8000").rstrip("/")
REQUEST_TIMEOUT_SECONDS = 18


def load_backend_env() -> dict[str, str]:
    values: dict[str, str] = {}
    env_path = ROOT / "Backend" / ".env"
    if not env_path.exists():
        return values
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        values[name.strip()] = value.strip().strip('"').strip("'")
    return values


def request(method: str, path: str, payload: dict | None = None) -> tuple[int, str]:
    body = None
    headers = {"Accept": "application/json"}
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(
        f"{BACKEND_URL}{path}",
        data=body,
        headers=headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            return response.status, response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as error:
        return 0, str(error.reason)


def preview(raw: str) -> str:
    try:
        data = json.loads(raw)
        if isinstance(data, dict):
            if "detail" in data:
                return f"detail={data['detail']}"
            if "message" in data:
                return f"message={data['message']}"
            if "languages" in data:
                return f"languages={len(data['languages'])}"
            if "parsed_problem" in data:
                return "parsed_problem=present"
            if "content" in data:
                return "content=present"
            if "verdict" in data:
                return f"verdict={data['verdict']}"
        return json.dumps(data, ensure_ascii=True)[:220]
    except json.JSONDecodeError:
        return raw.replace("\n", " ")[:220]


def check(name: str, method: str, path: str, payload: dict | None = None) -> bool:
    status, body = request(method, path, payload)
    passed = 200 <= status < 300
    label = "PASS" if passed else "FAIL"
    status_text = str(status) if status else "connection failed"
    print(f"[{label}] {name}: HTTP {status_text} | {preview(body)}")
    return passed


def main() -> int:
    env = load_backend_env()
    print(f"Backend: {BACKEND_URL}")
    print(f"Configured AI provider: {env.get('AI_BASE_URL', '<missing>')}")
    print(f"Configured AI model: {env.get('AI_MODEL', '<missing>')}")
    print(f"Server AI key: {'present' if env.get('AI_API_KEY') else 'missing'}")
    print()

    checks = [
        ("root", "GET", "/", None),
        ("health", "GET", "/health", None),
        ("supported languages", "GET", "/judge/supported-languages", None),
        (
            "run code",
            "POST",
            "/judge/run-code",
            {"source_code": "print('questide-check')", "language_id": 71, "stdin": ""},
        ),
        (
            "submit code",
            "POST",
            "/judge/submit",
            {
                "source_code": "print('questide-check')",
                "language_id": 71,
                "testcases": [
                    {
                        "id": 1,
                        "stdin": "",
                        "expected_output": "questide-check",
                        "is_hidden": False,
                    }
                ],
            },
        ),
        (
            "parse problem",
            "POST",
            "/parse-problem",
            {"problem_text": "Given an array of integers, return the largest value."},
        ),
        (
            "AI assistant",
            "POST",
            "/ai/assist",
            {
                "action": "hint",
                "problem_description": "Find the largest value in an array.",
                "user_code": "print(max([1, 2]))",
                "language": "python",
            },
        ),
    ]

    results = [check(*item) for item in checks]
    print(f"\nResult: {sum(results)}/{len(results)} endpoints passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
