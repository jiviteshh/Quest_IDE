import axios from "axios";
import type { AxiosRequestConfig } from "axios";
import type { RunCodeResponse, SubmitCodeResponse } from "@/src/types/judge";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

const aiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 120_000,
});

type AIRequestConfig = AxiosRequestConfig & {
  skipUserApiKey?: boolean;
};

aiClient.interceptors.request.use((config) => {
  if ((config as AIRequestConfig).skipUserApiKey) {
    return config;
  }

  const apiKey = typeof window !== "undefined"
    ? localStorage.getItem("questide_ai_api_key")
    : null;

  if (apiKey) {
    config.headers["x-user-api-key"] = apiKey;
  }

  return config;
});

export type AIAction =
  | "chat"
  | "hint"
  | "explain_approach"
  | "optimize"
  | "find_bug"
  | "complexity_analysis"
  | "explain_solution"
  | "generate_testcases";

export type FailedTestcaseContext = {
  input: string;
  expected_output: string;
  actual_output: string;
};

export type AIContextPayload = {
  problem_title?: string;
  problem_description?: string;
  user_code?: string;
  language?: string;
  last_verdict?: string | null;
  failed_testcase?: FailedTestcaseContext | null;
  latest_run_result?: RunCodeResponse | null;
  latest_run_suite_result?: SubmitCodeResponse | null;
  latest_submit_result?: SubmitCodeResponse | null;
  execution_metadata?: Record<string, string | number | boolean | null>;
};

export type AIRequest = {
  action: AIAction;
  query?: string;
  problem_description: string;
  user_code: string;
  language: string;
  failed_testcase?: FailedTestcaseContext | null;
  last_verdict?: string | null;
  context?: AIContextPayload;
};

function isUserApiKeyError(error: unknown): boolean {
  if (!axios.isAxiosError(error)) return false;
  const detail = (error.response?.data as { detail?: unknown } | undefined)?.detail;
  return typeof detail === "string" && /api[_ ]key/i.test(detail);
}

function clearStoredUserApiKey() {
  if (typeof window !== "undefined") {
    localStorage.removeItem("questide_ai_api_key");
  }
}

export type AIResponse = {
  content: string;
  action: AIAction;
  error?: string | null;
};

export async function requestAIAssist(payload: AIRequest): Promise<AIResponse> {
  try {
    const response = await aiClient.post<AIResponse>("/ai/assist", payload);
    return response.data;
  } catch (error) {
    if (isUserApiKeyError(error) && typeof window !== "undefined" && localStorage.getItem("questide_ai_api_key")) {
      clearStoredUserApiKey();
      try {
        const response = await aiClient.post<AIResponse>("/ai/assist", payload, {
          skipUserApiKey: true,
        } as AIRequestConfig);
        return response.data;
      } catch (fallbackError) {
        error = fallbackError;
      }
    }
    if (axios.isAxiosError(error)) {
      const data = error.response?.data as { detail?: string } | undefined;
      return {
        content: "",
        action: payload.action,
        error: data?.detail ?? error.message ?? "AI request failed.",
      };
    }
    return {
      content: "",
      action: payload.action,
      error: "AI request failed. Please try again.",
    };
  }
}
