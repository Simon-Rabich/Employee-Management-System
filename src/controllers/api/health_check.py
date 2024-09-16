from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.models.product_version import ProductVersion
from dtos.response_dto import ResponseDTO  # Importing from the dtos folder
from dtos.health_check_dto import HealthCheckDTO  # Importing from the dtos folder
from utils.format_response import format_response

router = APIRouter()


# Define the request body for environment
class EnvironmentRequest(BaseModel):
    environment: str


@router.post("/health", response_model=ResponseDTO)
def health_check(request: EnvironmentRequest, db: Session = Depends(get_db)) -> ResponseDTO:
    try:
        # Query the ProductVersion table for the specified environment
        latest_version = db.query(ProductVersion).filter_by(environment=request.environment).order_by(ProductVersion.build_time.desc()).first()

        # If no version is found for the environment, raise a 404
        if not latest_version:
            raise HTTPException(status_code=404, detail="No product version found for the specified environment")

        # Prepare the health check data
        health_data = HealthCheckDTO(
            status="healthy",
            version=latest_version.version,
            build_time=latest_version.build_time.strftime("%d/%m/%Y %H:%M:%S") if latest_version.build_time else None
        )

        # Use the Pydantic model in the response
        return format_response(success=True, result=health_data)
    except HTTPException as e:
        return format_response(success=False, error=e.detail)
    except Exception as e:
        return format_response(success=False, error=str(e))
