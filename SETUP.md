# QuestIDE Setup and Operations Guide

This guide explains how to run QuestIDE from a fresh Git clone on Windows.

## What QuestIDE Runs

Docker Compose starts three application services:

- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- Piston code execution: `http://localhost:2000`

A one-time bootstrap service installs the Python, Java, and GCC runtimes used by the code judge. Runtime packages are stored in a Docker volume and are reused on later starts.

## Requirements

Install these before starting:

- Docker Desktop
- Docker Desktop configured to use Linux containers
- Git
- At least 5 GB free disk space for Piston runtimes
- An API key from an OpenAI-compatible provider for AI features

Supported provider types include OpenAI, Groq, OpenRouter, DeepSeek, Together, and Ollama.

## First-Time Installation

Clone the repository and enter it:

```powershell
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Create the private backend configuration file:

```powershell
Copy-Item Backend/.env.example Backend/.env
```

Open `Backend/.env` and configure an AI provider. Example using Groq:

```env
AI_API_KEY=your_groq_key
AI_BASE_URL=https://api.groq.com/openai/v1
AI_MODEL=openai/gpt-oss-120b
```

Example using OpenAI:

```env
AI_API_KEY=your_openai_key
AI_BASE_URL=https://api.openai.com/v1
AI_MODEL=gpt-4o-mini
```

Do not change `PISTON_URL` when using Docker Compose. Compose supplies the internal Piston address to the backend automatically.

Start the complete application:

```powershell
docker compose up --build -d
```

The first startup may take several minutes while Docker builds the application images and Piston installs language runtimes.

Open the application:

```text
http://localhost:3000
```

## Check the Installation

View service status:

```powershell
docker compose ps
```

Expected services:

```text
questide-piston: healthy
questide-backend: running
questide-frontend: running
questide-piston-bootstrap: exited (0)
```

Check the frontend and backend:

```powershell
curl.exe -I http://localhost:3000
curl.exe http://localhost:8000/health
```

Check installed Piston runtimes:

```powershell
curl.exe http://localhost:2000/api/v2/runtimes
```

Run every backend endpoint smoke test:

```powershell
python check_endpoints.py
```

The checker must be run from the repository root. If `python` is not available on PATH, use the backend virtual environment Python or install Python separately.

## Daily Start

After the first installation, start the application with:

```powershell
cd YOUR_REPOSITORY_FOLDER
docker compose up -d
```

Then open:

```text
http://localhost:3000
```

No manual `uvicorn`, `npm`, or Piston command is required when using Docker Compose.

## Change AI Provider

Edit only these values in `Backend/.env`:

```env
AI_API_KEY=your_provider_key
AI_BASE_URL=provider_openai_compatible_url
AI_MODEL=provider_model_name
```

Restart the backend so it reloads the environment values:

```powershell
docker compose up -d --force-recreate backend
```

The Docker images do not need to be rebuilt for provider or key changes.

## Update the Application

Pull the latest Git changes:

```powershell
git pull origin main
```

Rebuild and restart application images:

```powershell
docker compose up --build -d
```

Keep `Backend/.env` locally. It is intentionally ignored by Git.

## Stop the Application

Stop containers while preserving Piston runtimes:

```powershell
docker compose down
```

Start again later with:

```powershell
docker compose up -d
```

Remove containers and downloaded Piston runtimes:

```powershell
docker compose down -v
```

Use `down -v` only when you intentionally want to download all runtimes again.

## Troubleshooting

### Docker daemon unavailable

Start Docker Desktop, wait until it reports that Docker is running, then retry:

```powershell
docker compose up -d
```

### Port already allocated

Check containers using the QuestIDE ports:

```powershell
docker ps -a
```

Stop the old containers or stop the complete previous stack:

```powershell
docker compose down
```

The required ports are `2000`, `3000`, and `8000`.

### Frontend cannot open

Check the frontend logs:

```powershell
docker compose logs --tail=100 frontend
```

Confirm the frontend responds:

```powershell
curl.exe -I http://localhost:3000
```

### AI parsing fails

Check backend logs:

```powershell
docker compose logs --tail=100 backend
```

Verify these values in `Backend/.env`:

```env
AI_API_KEY=
AI_BASE_URL=
AI_MODEL=
```

The provider URL and model must match each other. Restart the backend after changing them.

### Code execution fails

Check Piston:

```powershell
curl.exe http://localhost:2000/api/v2/runtimes
docker compose logs --tail=100 piston
```

If the runtime list is empty, restart the bootstrap service:

```powershell
docker compose run --rm piston-bootstrap
```

### Full clean reset

This removes containers, networks, and downloaded runtime packages:

```powershell
docker compose down -v --remove-orphans
docker compose up --build -d
```

## Safe Git Publishing

Never commit these files or directories:

```text
Backend/.env
Frontend/frontend/.env.local
Backend/venv/
Frontend/frontend/node_modules/
Frontend/frontend/.next/
**/__pycache__/
```

Check the repository before committing:

```powershell
git status --short
git check-ignore -v Backend/.env Frontend/frontend/.env.local
```

Commit and push from the repository root:

```powershell
git add .
git commit -m "Prepare QuestIDE release"
git push origin main
```

Authenticate with GitHub through Git Credential Manager or a GitHub Personal Access Token. Never put a token in a Git remote URL or commit it to a file.

## Docker Image Notes

The Compose file builds the latest QuestIDE backend and frontend images locally. Piston is pulled from:

```text
jivitesh09/questide-piston:latest
```

API keys are injected into the backend container at runtime from `Backend/.env`; they are not included in the application images.
