from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/health/db", tags=["Health"])
def database_health_placeholder() -> dict[str, str]:
    # The real database connectivity check is added with the DB setup stage.
    return {"status": "database check not implemented yet"}
