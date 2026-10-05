from decimal import Decimal

from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    email: str
    salary: Decimal


class EmployeeUpdate(BaseModel):
    name: str
    email: str
    salary: Decimal