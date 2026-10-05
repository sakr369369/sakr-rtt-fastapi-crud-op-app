from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    salary: Decimal

    model_config = ConfigDict(from_attributes=True)