from sqlalchemy import Column, Integer, String, Numeric

from app.config.database import Base


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    salary = Column(Numeric(10, 2), nullable=False)