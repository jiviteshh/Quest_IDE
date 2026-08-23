# c:\Users\jivin\Documents\AI CODING\Backend\app\config.py
"""Application configuration for execution providers and constants."""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()

# Provider endpoint and auth
_piston_env = os.getenv("PISTON_URL", "http://16.112.68.119:2000")
PISTON_URL = _piston_env if _piston_env.endswith("/api/v2/execute") else f"{_piston_env.rstrip('/')}/api/v2/execute"
PISTON_API_KEY = os.getenv("PISTON_API_KEY", "")

# Upstream execution timeout in seconds
EXECUTION_TIMEOUT_SECONDS = 15

# OpenAI-compatible provider settings. Legacy NVIDIA names remain as fallbacks
# so existing installations continue working while migrating configuration.
AI_BASE_URL = os.getenv("AI_BASE_URL", os.getenv("NVIDIA_API_BASE_URL", "https://api.openai.com/v1"))
AI_MODEL = os.getenv("AI_MODEL", os.getenv("NVIDIA_MODEL", "gpt-4o-mini"))
AI_TEMPERATURE = float(os.getenv("AI_TEMPERATURE", os.getenv("NVIDIA_TEMPERATURE", "0")))
AI_TOP_P = float(os.getenv("AI_TOP_P", os.getenv("NVIDIA_TOP_P", "1")))
AI_MAX_TOKENS = int(os.getenv("AI_MAX_TOKENS", os.getenv("NVIDIA_MAX_TOKENS", "4096")))
LLM_TIMEOUT_SECONDS = int(os.getenv("LLM_TIMEOUT_SECONDS", "90"))

# Language mapping kept provider-agnostic by using internal language IDs.
# These IDs match common Judge0 ids, which eases future migration.
LANGUAGE_MAP: dict[int, dict[str, str]] = {
    71: {"language": "python", "version": "3.10.0"},
    62: {"language": "java", "version": "15.0.2"},
    54: {"language": "c++", "version": "10.2.0"},
}
