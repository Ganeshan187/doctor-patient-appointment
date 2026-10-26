
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from app.models.base import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )

    full_name = Column(String(100), nullable=False)
    specialization = Column(String(100), nullable=False)
    license_number = Column(String(100), unique=True, nullable=False)

    user = relationship("User")
