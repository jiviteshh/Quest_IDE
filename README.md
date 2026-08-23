# QuestIDE ⚡

### AI-Native Coding Workspace for Modern Problem Solving

QuestIDE is an **AI-native coding workspace** that transforms raw coding problems into complete, interactive coding environments.

Instead of switching between an AI assistant, code editor, compiler, terminal, and manually created testcase files, QuestIDE brings the entire problem-solving workflow into one workspace.

> **Paste a problem → Generate the workspace → Code → Run → Debug → Submit**

---

## 🚀 Why QuestIDE?

During coding interviews, online assessments, competitive programming, and DSA practice, developers often face a fragmented workflow:

* The exact problem may not exist on platforms like LeetCode.
* Custom or company-specific problems require manual setup.
* Testcases often need to be created manually.
* Edge cases have to be identified and verified separately.
* Developers switch between editors, compilers, terminals, and AI tools.
* Generic AI assistants often lack awareness of the current code and execution state.

QuestIDE addresses this by turning **any coding problem into an executable and context-aware coding workspace**.

---

## ✨ Core Features

### 🤖 AI-Powered Problem Parsing

Provide a raw coding problem and QuestIDE generates structured information including:

* Problem metadata
* Constraints
* Input/output format
* Starter code
* Visible testcases
* Hidden testcases

The AI converts unstructured problem descriptions into a format that the coding workspace can immediately use.

### 💻 Integrated Monaco IDE

QuestIDE provides a browser-based coding environment powered by **Monaco Editor** with:

* Syntax highlighting
* Multiple programming languages
* Starter templates
* Code editing
* Custom input execution
* Run and Submit workflows

### 🧪 Testcase & Evaluation System

QuestIDE supports:

* Public/visible testcases
* Hidden testcases
* Custom input
* Output comparison
* Testcase-level results
* Execution verdicts

This allows users to test their solutions before submitting them against hidden evaluation cases.

### 🤖 Quest AI

Quest AI is a contextual coding assistant that can work with:

* Current problem
* Active code
* Execution output
* Failed testcases
* Debugging context

It can assist with:

* Debugging
* Logic explanation
* Edge-case reasoning
* Optimization
* Time-complexity analysis
* Interview-style hints

The goal is to provide **contextual guidance rather than simply generating the complete solution**.

### 🌍 Multi-Language Execution

QuestIDE is designed to support multiple programming languages through the execution infrastructure.

Current workspace support includes languages such as:

* Python
* Java
* C++

### 🔐 Isolated Code Execution

User code is executed through **Piston and Docker-based runtime infrastructure**, separating code execution from the main application.

This provides a foundation for safely handling user-submitted code and managing language-specific runtimes.

---

# 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │      QuestIDE       │
                         │    Next.js Web App  │
                         └──────────┬──────────┘
                                    │
                                    │ REST API
                                    ▼
                         ┌─────────────────────┐
                         │    FastAPI Backend  │
                         │                     │
                         │  Parser             │
                         │  AI Assistant       │
                         │  Judge              │
                         │  Evaluation         │
                         └───────┬───────┬─────┘
                                 │       │
                   ┌─────────────┘       └──────────────┐
                   ▼                                    ▼
          ┌─────────────────┐                  ┌─────────────────┐
          │ OpenAI-Compatible│                  │ Piston Execution│
          │   AI Provider    │                  │     Engine      │
          └─────────────────┘                  └────────┬────────┘
                                                         │
                                                         ▼
                                                ┌─────────────────┐
                                                │ Docker Runtimes │
                                                │                 │
                                                │ Python / Java   │
                                                │ C++ / ...       │
                                                └─────────────────┘
```

---

# 🧠 AI Architecture

QuestIDE uses **OpenAI-compatible APIs** for its AI integration.

The application is intentionally designed around a provider-compatible interface rather than tightly coupling the system to a single AI provider.

This makes it possible to switch between compatible models or providers while keeping the core QuestIDE architecture unchanged.

### AI Workflow

```text
Raw Problem
     │
     ▼
AI Problem Parser
     │
     ├── Problem Metadata
     ├── Constraints
     ├── Starter Code
     ├── Visible Testcases
     └── Hidden Testcases
              │
              ▼
        QuestIDE Workspace
              │
              ▼
          User Code
              │
              ▼
       Piston / Docker
              │
              ▼
       Execution Result
              │
              ├── Passed
              ├── Failed
              └── Runtime Error
                       │
                       ▼
                  Quest AI
                       │
                       ▼
             Contextual Guidance
```

---

# 🛠️ Tech Stack

## Frontend

* Next.js
* React
* TypeScript
* Monaco Editor
* Tailwind CSS

## Backend

* Python
* FastAPI
* Pydantic
* REST APIs

## AI

* OpenAI-compatible APIs
* Configurable LLM provider/model
* Structured AI problem parsing
* Context-aware AI assistance

## Code Execution

* Piston Execution Engine
* Docker
* Language-specific runtimes

## Deployment

* Vercel — Frontend
* AWS EC2 — Backend & execution infrastructure
* Docker — Runtime isolation
* Ngrok — Secure HTTPS tunneling during production deployment

---

# 📁 Project Structure

```text
AI CODING/
│
├── Backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   │
│   │   ├── models/
│   │   │   └── schemas.py
│   │   │
│   │   ├── prompts/
│   │   │   └── parser_prompt.txt
│   │   │
│   │   ├── routes/
│   │   │   ├── ai.py
│   │   │   ├── health.py
│   │   │   ├── judge.py
│   │   │   └── parser.py
│   │   │
│   │   ├── services/
│   │   │   ├── ai_service.py
│   │   │   ├── evaluation_service.py
│   │   │   ├── judge_service.py
│   │   │   └── llm_service.py
│   │   │
│   │   └── utils/
│   │       └── helpers.py
│   │
│   ├── .env
│   ├── .env.example
│   ├── requirements.txt
│   └── README.md
│
├── Frontend/
│   └── frontend/
│       ├── app/
│       │   ├── layout.tsx
│       │   ├── page.tsx
│       │   ├── globals.css
│       │   └── workspace/
│       │       └── page.tsx
│       │
│       ├── public/
│       │   ├── logo.png
│       │   └── SVG assets
│       │
│       ├── src/
│       │   ├── app/
│       │   │   ├── page.tsx
│       │   │   └── workspace/
│       │   │       └── page.tsx
│       │   │
│       │   ├── components/
│       │   ├── hooks/
│       │   ├── lib/
│       │   ├── styles/
│       │   └── types/
│       │
│       ├── package.json
│       ├── next.config.ts
│       └── tsconfig.json
│
├── docker-compose.yml
├── Dockerfile
├── check_endpoints.py
├── README.md
└── SETUP.md
```

---

# 📂 Backend

The FastAPI backend handles the core application logic, including:

* AI problem parsing
* AI assistant requests
* Code execution
* Submission judging
* Testcase evaluation
* Health monitoring

### `app/main.py`

Initializes the FastAPI application and registers API routes.

### `app/config.py`

Manages environment configuration such as:

* AI provider URL
* Model name
* API key
* Piston URL
* Request timeouts
* Runtime configuration

### `app/models/schemas.py`

Contains Pydantic models used for:

* Problem parsing
* Testcases
* Code execution
* Submission requests
* Judge responses
* AI requests/responses

### `app/routes/`

API endpoint definitions.

| File        | Responsibility        |
| ----------- | --------------------- |
| `parser.py` | Problem parsing       |
| `judge.py`  | Run and submit code   |
| `ai.py`     | Quest AI endpoints    |
| `health.py` | Service health checks |

### `app/services/`

Contains the application's business logic.

| Service                 | Responsibility                  |
| ----------------------- | ------------------------------- |
| `llm_service.py`        | Communication with the AI model |
| `ai_service.py`         | Quest AI logic                  |
| `judge_service.py`      | Piston/execution integration    |
| `evaluation_service.py` | Testcase and output evaluation  |

### `app/prompts/parser_prompt.txt`

Contains the prompt used to convert raw coding problems into structured data.

---

# 🎨 Frontend

The frontend is built using **Next.js, React, TypeScript, Monaco Editor, and Tailwind CSS**.

### `app/`

Contains the Next.js App Router structure and application entry points.

### `src/components/`

Reusable UI components including:

* Code editor
* Problem panel
* AI assistant
* Navigation
* Workspace layout
* Testcase panel
* Verdict panel
* Modals
* Toast notifications

### `src/hooks/`

Custom React hooks for functionality such as:

* Workspace state
* Autosave
* API key storage
* Keyboard shortcuts
* Submission history
* Toast state

### `src/lib/`

Frontend utilities and API clients.

| File                   | Responsibility                |
| ---------------------- | ----------------------------- |
| `api.ts`               | Backend API communication     |
| `ai-service.ts`        | AI assistant requests         |
| `problem-storage.ts`   | Parsed problem persistence    |
| `workspace-storage.ts` | Workspace/autosave management |
| `languages.ts`         | Supported language metadata   |
| `templates.ts`         | Starter code templates        |

### `src/types/`

TypeScript definitions for:

* Parser data
* Judge responses
* Testcases
* Execution results
* Workspace state

---

# 🐳 Docker & Execution Infrastructure

QuestIDE uses **Docker-based execution infrastructure** together with Piston.

The execution flow is:

```text
User Code
    │
    ▼
FastAPI Backend
    │
    ▼
Piston
    │
    ▼
Docker Runtime
    │
    ▼
Language Execution
    │
    ▼
Output / Error
    │
    ▼
Evaluation Service
    │
    ▼
QuestIDE Verdict
```

This architecture provides isolation between user-submitted programs and the main application.

---

# 🔐 Environment Variables

Create a `.env` file inside the backend directory.

Example:

```env
AI_API_KEY=your_api_key
AI_BASE_URL=your_openai_compatible_api_url
AI_MODEL=your_model_name

PISTON_URL=http://localhost:2000

REQUEST_TIMEOUT=60
```

> Never commit your `.env` file or API keys to GitHub.

Use `.env.example` as the template for required configuration.

---

# ⚙️ Local Setup

## 1. Clone the repository

```bash
git clone <your-repository-url>

cd "AI CODING"
```

## 2. Configure the Backend

```bash
cd Backend

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your environment file:

```bash
cp .env.example .env
```

Update the AI and Piston configuration.

---

## 3. Start the FastAPI Backend

From the `Backend` directory:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

FastAPI documentation:

```text
http://localhost:8000/docs
```

---

## 4. Start the Frontend

```bash
cd Frontend/frontend

npm install

npm run dev
```

The frontend will be available at:

```text
http://localhost:3000
```

---

# 🧪 Testing Backend Endpoints

The project includes:

```text
check_endpoints.py
```

This utility can be used to verify that backend endpoints are responding correctly.

Example:

```bash
python check_endpoints.py
```

---

# 🔌 API Overview

QuestIDE exposes APIs for the major platform workflows.

### Problem Parser

```text
POST /parse-problem
```

Converts a raw problem statement into structured coding data.

### Code Execution

Judge endpoints handle:

* Running code
* Custom input
* Public testcases
* Submission execution

### AI Assistant

AI endpoints provide contextual assistance using the current coding context.

### Health

```text
GET /health
```

Used to verify backend/service availability.

---

# 🌐 Production Architecture

QuestIDE has been deployed using a distributed deployment setup:

```text
                    Internet
                       │
                       ▼
              ┌─────────────────┐
              │ Vercel Frontend │
              │     Next.js     │
              └────────┬────────┘
                       │ HTTPS
                       ▼
              ┌─────────────────┐
              │   AWS EC2       │
              │    FastAPI      │
              └───────┬─────────┘
                      │
              ┌───────┴────────┐
              ▼                ▼
      ┌──────────────┐  ┌───────────────┐
      │ OpenAI-      │  │    Piston     │
      │ Compatible   │  │    Engine     │
      │ AI Provider  │  └───────┬───────┘
      └──────────────┘          │
                                ▼
                         ┌──────────────┐
                         │    Docker    │
                         │   Runtimes   │
                         └──────────────┘
```

During deployment, challenges involving CORS, HTTPS/HTTP communication, AWS networking, Docker runtimes, and production API routing were addressed to bring the platform online.

---

# 🧠 Engineering Challenges

Building QuestIDE involved several real-world engineering challenges.

### 1. Secure Code Execution

Running arbitrary user code requires isolation and resource management.

**Solution:** Piston + Docker-based execution infrastructure.

### 2. AI Problem Structuring

Raw problem statements can be inconsistent and unstructured.

**Solution:** AI-powered parsing with structured output schemas and dedicated prompts.

### 3. Contextual AI

A generic chatbot cannot understand the complete state of a coding session.

**Solution:** Provide the assistant with relevant problem, code, execution, and testcase context.

### 4. Multi-Provider AI Architecture

Tightly coupling the application to a single model provider makes future model changes difficult.

**Solution:** Use an OpenAI-compatible API layer so compatible providers/models can be swapped with minimal application changes.

### 5. Production Deployment

The platform required multiple independent services to communicate correctly.

Challenges included:

* AWS EC2 networking
* Docker configuration
* Piston setup
* Runtime installation
* CORS
* HTTPS/HTTP conflicts
* Frontend/backend routing
* Secure API communication

---

# 🔮 Future Roadmap

QuestIDE is designed to evolve beyond a single coding workspace.

Potential future improvements include:

* Scalable execution workers
* Asynchronous execution queues
* Automatic worker scaling
* Load balancing
* Persistent user accounts
* Coding-session history
* Advanced evaluation analytics
* Company-specific assessment environments
* AI-generated interview rounds
* Adaptive difficulty
* Interviewer dashboards
* Team/organization workspaces
* Real-time collaborative coding
* Stronger sandbox security and resource limits

---

# 🎯 Vision

QuestIDE started from a simple problem:

> **Why should solving one custom coding problem require five different tools?**

The long-term vision is to build an **AI-native infrastructure for creating, solving, conducting, and evaluating coding problems**.

Instead of treating AI as a separate chatbot, QuestIDE integrates AI directly into the coding workflow.

```text
Problem
   ↓
AI Understanding
   ↓
Interactive Workspace
   ↓
Code Execution
   ↓
Evaluation
   ↓
Contextual AI Assistance
   ↓
Better Problem Solving
```

---


---

# 👨‍💻 Built With

**Next.js • TypeScript • React • Monaco Editor • Tailwind CSS • FastAPI • Python • OpenAI-Compatible APIs • Piston • Docker • AWS EC2 • Vercel**

---

## ⭐ QuestIDE

**Code. Solve. Debug. Level Up.**
