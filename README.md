# QuestIDE

Self-hosted AI coding workspace with problem parsing, code execution, testcase validation, and AI assistance.

## Requirements

- Docker Desktop with Linux containers enabled
- An API key from an OpenAI-compatible AI provider for AI features
- At least 5 GB free disk space for Piston language runtimes

## Start

From the repository root:

```powershell
docker compose up --build -d
```

Open <http://localhost:3000>.

The first startup installs the Python, Java, and C++ runtimes for Piston. This may take several minutes. Later starts are faster because runtimes are kept in a Docker volume.

## Configure AI

Copy the example configuration:

```powershell
Copy-Item Backend/.env.example Backend/.env
```

Edit `Backend/.env` and set the provider values:

```env
AI_API_KEY=your_provider_key
AI_BASE_URL=https://api.groq.com/openai/v1
AI_MODEL=openai/gpt-oss-120b
```

Restart the backend after changing provider settings:

```powershell
docker compose up -d --force-recreate backend
```

QuestIDE supports OpenAI-compatible providers such as OpenAI, Groq, OpenRouter, DeepSeek, Together, and Ollama. See `Backend/.env.example` for presets.

## Check Services

```powershell
docker compose ps
```

Run all API checks:

```powershell
python check_endpoints.py
```

Useful URLs:

- Frontend: <http://localhost:3000>
- Backend: <http://localhost:8000>
- Backend health: <http://localhost:8000/health>
- Piston runtimes: <http://localhost:2000/api/v2/runtimes>

## Stop and Reset

Stop the application:

```powershell
docker compose down
```

Remove the downloaded Piston runtimes as well:

```powershell
docker compose down -v
```

Do not share or commit `Backend/.env`. It contains a private API key.
