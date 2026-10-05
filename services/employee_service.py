from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository
from app.exceptions.employee_not_found_exception import EmployeeNotFoundException
from app.schemas.employee_request import (
    EmployeeCreate,
    EmployeeUpdate
)


class EmployeeService:

    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def create_employee(self, employee_request: EmployeeCreate) -> Employee:

        employee = Employee(
            name=employee_request.name,
            email=employee_request.email,
            salary=employee_request.salary
        )

        return self.repository.save(employee)

    def get_all_employees(self) -> list[Employee]:
        return self.repository.find_all()

    def get_employee_by_id(self, employee_id: int) -> Employee:

        employee = self.repository.find_by_id(employee_id)

        if employee is None:
            raise EmployeeNotFoundException(employee_id)

        return employee

    def update_employee(
            self,
            employee_id: int,
            employee_request: EmployeeUpdate
    ) -> Employee:

        employee = self.repository.find_by_id(employee_id)

        if employee is None:
            raise EmployeeNotFoundException(employee_id)

        employee.name = employee_request.name
        employee.email = employee_request.email
        employee.salary = employee_request.salary

        return self.repository.update(employee)

    def delete_employee(self, employee_id: int):

        employee = self.repository.find_by_id(employee_id)

        if employee is None:
            raise EmployeeNotFoundException(employee_id)

        self.repository.delete(employee)