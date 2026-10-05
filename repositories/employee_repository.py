from sqlalchemy.orm import Session

from app.models.employee import Employee


class EmployeeRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, employee: Employee) -> Employee:
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def find_all(self) -> list[Employee]:
        return self.db.query(Employee).all()

    def find_by_id(self, employee_id: int) -> Employee | None:
        return (
            self.db.query(Employee)
            .filter(Employee.id == employee_id)
            .first()
        )

    def update(self, employee: Employee) -> Employee:
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def delete(self, employee: Employee) -> None:
        self.db.delete(employee)
        self.db.commit()