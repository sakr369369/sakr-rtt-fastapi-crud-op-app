from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.employee_not_found_exception import (
    EmployeeNotFoundException
)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(EmployeeNotFoundException)
    async def employee_not_found_exception_handler(
        request: Request,
        exc: EmployeeNotFoundException
    ):

        return JSONResponse(

    status_code=404,

    content={

        "success": False,

        "status": 404,

        "message": exc.message,

        "data": None

    }

)