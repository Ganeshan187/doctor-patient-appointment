# Doctor Appointment API

A modular FastAPI starter project using PostgreSQL, SQLAlchemy 2.x, Alembic, Pydantic Settings, Argon2 password hashing, and JWT.

## Requirements

- Python 3.11+
- Docker Desktop (or Docker Engine with Compose)
- Git (optional)

## 1. Create your environment file

Copy `.env.example` to `.env`, then replace `JWT_SECRET_KEY` with a long random secret.

Linux/macOS/WSL:
```bash
cp .env.example .env
```

PowerShell:
```powershell
Copy-Item .env.example .env
```

Generate a secret with Python:
```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

## 2. Create and activate a virtual environment

Linux/macOS/WSL:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:
```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## 4. Start PostgreSQL

```bash
docker compose up -d db
docker compose ps
```

The local development database is configured by the URL in `.env.example`. Change the password in both `compose.yaml` and `.env` if you change it.

## 5. Run the API

```bash
uvicorn app.main:app --reload
```

Open:
- API docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health
- Database check: http://127.0.0.1:8000/health/db

## 6. Database migrations

Alembic is included. After adding SQLAlchemy models, initialize migration configuration if needed:
```bash
alembic init alembic
```
Then configure `alembic/env.py` to import `Base` and your models, and use the database URL from settings before generating migrations. Migration wiring will be completed in the next implementation stage.

## Project layout

- `app/api/`: API routers and dependency injection
- `app/core/`: settings and security helpers
- `app/db/`: SQLAlchemy base and database session
- `app/models/`: database entities
- `app/schemas/`: request/response schemas
- `app/repositories/`: database query/persistence layer
- `app/services/`: business logic
- `tests/`: automated tests

This is a starter scaffold, not yet a complete appointment system. Authentication, models, availability, booking, cancellation, ranking, and their tests will be implemented in the next stages.
