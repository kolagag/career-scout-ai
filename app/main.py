"""FastAPI application entry point for CareerScout AI."""

from fastapi import FastAPI
from dotenv import load_dotenv

# Load local development settings when a .env file is present. Environment
# variables already supplied by the runtime take precedence.
load_dotenv()

app = FastAPI(
    title="CareerScout AI",
    version="0.1.0",
    description="Foundation API for an AI-powered career assistant.",
)


@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    """Return a lightweight liveness response for health probes."""
    return {"status": "ok"}
