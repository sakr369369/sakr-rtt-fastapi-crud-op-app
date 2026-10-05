from fastapi import Depends

from app.dependencies.repository_dependency import (
    get_employee_repository
)

from app.repositories.employee_repository import (
    EmployeeRepository
)

from app.services.employee_service import EmployeeService


def get_employee_service(
        repository: EmployeeRepository =
        Depends(get_employee_repository)
):
    return EmployeeService(repository)