from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.v1 import heath_routes

app = FastAPI(title="Doctor Appointment API")


app.include_router(heath_routes.router)
