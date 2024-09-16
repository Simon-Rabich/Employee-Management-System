from fastapi import FastAPI
import logging
from sqlalchemy import exc
from src.database.connection import engine, Base
from src.controllers.api.employee_entity import router as employee_router
from src.controllers.api.health_check import router as health_check_router
from src.controllers.api.add_product_version import router as product_version_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Include the health check router
app.include_router(health_check_router)


@app.on_event("startup")
def on_startup():
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully.")
    except exc.SQLAlchemyError as e:
        logger.error("Failed to create database tables.")
        logger.error(e)
        raise e


@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Include the employee router
app.include_router(employee_router, prefix="/api")
app.include_router(product_version_router, prefix="/api")
