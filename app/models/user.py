
from enum import Enum as PyEnum

from sqlalchemy import Column, Integer, String, Boolean, Enum

from app.models.base import Base


class UserRole(PyEnum):
    DOCTOR = "doctor"
    PATIENT = "patient"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    role = Column(Enum(UserRole, name="user_role"), nullable=False,)

    is_active = Column(Boolean, default=False, nullable=False, server_default="false",)

    is_email_verified = Column(Boolean, default=False, nullable=False, server_default="false",)
