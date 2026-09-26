# CareerScout AI

Day 1 foundation for a future agentic AI career assistant. This repository currently exposes only a FastAPI application and a liveness endpoint. It deliberately includes no AI providers, databases, authentication, job scraping, or external integrations.

## Requirements

- Python 3.11+
- `pip`

## Setup

Create and activate a virtual environment:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Optionally copy the environment template for future local configuration:

```bash
cp .env.example .env
```

## Run locally

```bash
uvicorn app.main:app --reload
```

The service runs at `http://127.0.0.1:8000`. Confirm it is live:

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Test

```bash
pytest
```

## Project layout

- `app/main.py` — application factory module and health endpoint.
- `app/models/` — Pydantic request and response contracts, including `CandidateProfile`.
- `app/api/` — reserved for HTTP route modules.
- `app/services/` — reserved for application service logic.
- `app/agents/` — reserved for future agent orchestration.
- `app/tools/` — reserved for future agent tool adapters.
- `app/core/` — reserved for shared configuration and infrastructure code.
- `tests/` — automated tests.
- `docs/` — project documentation.
- `data/` — local runtime data only; ignored by Git except its placeholder.
