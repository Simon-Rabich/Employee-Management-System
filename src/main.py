from fastapi import FastAPI
from src.database.connection import Base, engine
from src.controllers.employee_api import router as employee_router

tags_metadata = [
    {
        "name": "employees",
        "description": "Operations with employees. The **read** operation can be done by anyone.",
    }
]

app = FastAPI(
    title="Employee Management System API",
    description="API for managing employees",
    version="1.0.0",
    docs_url="/documentation",  # Customize the URL path for Swagger UI
    redoc_url="/redocumentation",  # Customize the URL path for ReDoc
)

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Include the router from the employee API
app.include_router(employee_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee Management System"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main_api:app", host="127.0.0.1", port=8000, reload=True)
