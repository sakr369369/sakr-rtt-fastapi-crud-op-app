from fastapi import FastAPI

from app.controllers.employee_controller import router
from app.exceptions.global_exception_handler import register_exception_handlers

app = FastAPI()

register_exception_handlers(app)

app.include_router(router)