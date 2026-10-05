from fastapi import APIRouter, Depends, status

from app.common.api_response import ApiResponse
from app.dependencies.service_dependency import get_employee_service

from app.schemas.employee_request import (
    EmployeeCreate,
    EmployeeUpdate
)

from app.schemas.employee_response import EmployeeResponse

from app.services.employee_service import EmployeeService


router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post(
    "",
    response_model=ApiResponse[EmployeeResponse],
    status_code=status.HTTP_201_CREATED
)
def create_employee(
    request: EmployeeCreate,
    service: EmployeeService = Depends(get_employee_service)
):
   return ApiResponse(

    success=True,

    status=201,

    message="Employee created successfully.",

    data=service.create_employee(request)

)


@router.get(
    "",
    response_model=ApiResponse[list[EmployeeResponse]],
    status_code=status.HTTP_200_OK
)
def get_all_employees(
    service: EmployeeService = Depends(get_employee_service)
):
    employee = service.get_all_employees()
    return ApiResponse(
    success=True,
    status=200,
    message="Employee fetched successfully.",
    data=employee
)


@router.get(
    "/{employee_id}",
    response_model=ApiResponse[EmployeeResponse],
    status_code=status.HTTP_200_OK
)
def get_employee_by_id(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service)
):
    employee = service.get_employee_by_id(employee_id)
    
    return ApiResponse(
    success=True,
    status=200,
    message="Employee fetched successfully.",
    data=employee
)


@router.put(
    "/{employee_id}",
    response_model=ApiResponse[EmployeeResponse],
    status_code=status.HTTP_200_OK
)
def update_employee(
    employee_id: int,
    request: EmployeeUpdate,
    service: EmployeeService = Depends(get_employee_service)
):
    employee = service.update_employee(employee_id, request)
    return ApiResponse(
    success=True,
    status=200,
    message="Employee updated successfully.",
    data=employee
)


@router.delete(
    "/{employee_id}",
    status_code=status.HTTP_200_OK
)
def delete_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service)
):
    service.delete_employee(employee_id)
    return ApiResponse(
        success=True,
        status=200,
        message="Employee deleted successfully.",
        data=None
    )