from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.models.product_version import ProductVersion
from dtos.response_dto import ResponseDTO
from dtos.health_check_dto import HealthCheckDTO
from utils.format_response import format_response

router = APIRouter()


@router.get("/health", response_model=ResponseDTO)
def health_check(db: Session = Depends(get_db)) -> ResponseDTO:
    try:
        # Get the latest product version information
        latest_version = db.query(ProductVersion).order_by(ProductVersion.build_time.desc()).first()

        # Prepare the health check data
        health_data = HealthCheckDTO(
            status="healthy",
            version=latest_version.version if latest_version else None,
            buildTime=latest_version.build_time.strftime("%d/%m/%Y %H:%M:%S") if latest_version else None
        )

        return format_response(success=True, result=health_data)
    except Exception as e:
        return format_response(success=False, error=str(e))

