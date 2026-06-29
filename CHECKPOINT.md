# Smart Spend Tracker Checkpoint

Date: 2026-06-26

## What this repo is

`smart_spend_tracker` is a small expense-tracking app scaffold with:

- A Python FastAPI backend
- Alembic migrations for PostgreSQL
- A Docker Compose file for a Postgres service
- An empty `frontend/` folder at the moment

## Backend summary

Location: `backend/`

Main stack:

- FastAPI
- SQLAlchemy 2 async
- asyncpg
- Alembic
- Pydantic Settings

Entry point:

- `backend/src/app/main.py`

Current API:

- `GET /health` returns `{"status": "ok", "environment": settings.environment}`
- `POST /expenses/` creates an expense
- `GET /expenses/` lists expenses

Architecture:

- `src/app/core/config.py` loads settings from `.env`
- `src/app/core/db.py` creates the async SQLAlchemy engine and session dependency
- `src/app/shared/base.py` defines the declarative ORM base
- `src/app/modules/expenses/` contains the expense feature split into:
  - `models.py` ORM model
  - `schemas.py` request/response schemas
  - `repository.py` DB access
  - `service.py` thin business layer
  - `router.py` FastAPI routes

Database model:

- Table: `expenses`
- Fields:
  - `id` UUID primary key
  - `title` string(255)
  - `amount` numeric(12,2)
  - `category` string(100)
  - `created_at` timezone datetime default `now()`

Migration state:

- One initial migration exists:
  - `backend/migrations/versions/42608b320693_create_expenses_table.py`

## Infra summary

Location: `infra/`

- `docker-compose.yaml` runs PostgreSQL 17 Alpine
- Database credentials in compose:
  - user: `spend`
  - password: `spend`
  - database: `spend_tracker`
- Port mapped: `5432:5432`

## Frontend summary

Location: `frontend/`

- No source files were present when I checked
- Treat this as a placeholder or unfinished app shell

## Important details

- Backend Python version: `>=3.13`
- Backend `.env` is required because `database_url` has no default
- The backend `README.md` is currently empty
- Alembic env points at `src.app` imports and uses `settings.database_url`

## Reusable checkpoint prompt

If you want to continue later, paste this:

```text
Use the Smart Spend Tracker checkpoint.
Repo shape: FastAPI backend in backend/, empty frontend/, Postgres in infra/docker-compose.yaml.
Backend entry point is backend/src/app/main.py.
It exposes GET /health, POST /expenses/, and GET /expenses/.
Expense model fields are id, title, amount, category, created_at.
Ask me to continue from the checkpoint and inspect or modify the relevant files.
```

