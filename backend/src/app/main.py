
from contextlib import asynccontextmanager

from app.core.middleware import RequestLoggingMiddleware
from fastapi import FastAPI

from app.core.config import settings

from app.modules.expenses.router import router as expenses_router
from .core.exception_handlers import app_exception_handler, unhandled_exception_handler
from .shared.exception import AppException
from app.core.logging import configure_logging, log

configure_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("app_started", environment=settings.environment)
    yield
    log.info("app_stopped")


app = FastAPI(title=settings.app_name)


app.add_middleware(RequestLoggingMiddleware)
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)
app.include_router(expenses_router)

@app.get("/health")
def health_check():
    return {"status": "ok", "environment": settings.environment}