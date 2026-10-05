from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.repositories.employee_repository import EmployeeRepository


def get_employee_repository(
        db: Session = Depends(get_db)
):
    return EmployeeRepository(db)