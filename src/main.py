from fastapi import FastAPI, Response
import logging
from sqlalchemy import exc
from src.database.connection import engine, Base
from src.controllers.api.employee_entity import router as employee_router
from src.controllers.api.health_check import router as health_check_router
from src.controllers.api.add_product_version import router as product_version_router

import psutil
from src.metrics import CPU_USAGE, MEMORY_USAGE, NETWORK_IO_COUNTERS, SITE_VISITS
from src.middleware.api_call_middleware import APICallMiddleware
import prometheus_client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Include routers
app.include_router(health_check_router)
app.include_router(employee_router, prefix="/api")
app.include_router(product_version_router, prefix="/api")

# Add the custom middleware
app.add_middleware(APICallMiddleware)


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


@app.get("/metrics")
def metrics():
    # Update metrics before serving
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.virtual_memory().used)
    net_io = psutil.net_io_counters()
    NETWORK_IO_COUNTERS.labels('in').set(net_io.bytes_recv)
    NETWORK_IO_COUNTERS.labels('out').set(net_io.bytes_sent)

    return Response(prometheus_client.generate_latest(), media_type='text/plain')
