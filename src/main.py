import logging
from fastapi import FastAPI
from sqlalchemy import exc
from src.database.connection import engine, Base
from src.controllers.employee_api import router as employee_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

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
