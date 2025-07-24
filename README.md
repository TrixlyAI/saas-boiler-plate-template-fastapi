# SaaS Boilerplate for Voice AI Engine

This project is a boilerplate for building SaaS applications with a Voice AI engine backend using FastAPI.

## Features
- Multi-tenant user authentication
- Subscription and billing ready
- Voice AI API endpoints
- Background task processing
- Modular, scalable structure

## Structure
- `app/` - Main backend application
- `tests/` - Unit and integration tests
- `alembic/` - Database migrations

## Getting Started
1. Copy `.env.example` to `.env` and configure your environment variables.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `uvicorn app.main:app --reload` 