from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.models.product_version import ProductVersion
from dtos.response_dto import ResponseDTO
from utils.format_response import format_response

router = APIRouter()


# Define the request body model
class ProductVersionRequest(BaseModel):
    environment: str
    version: str
    build_time: Optional[datetime] = None  # Optional build_time


@router.post("/product_version", response_model=ResponseDTO)
def add_product_version(
        request: ProductVersionRequest,
        db: Session = Depends(get_db)
) -> ResponseDTO:
    try:
        # If build_time is not provided, default to the current time
        build_time = request.build_time or datetime.now()

        new_version = ProductVersion(
            environment=request.environment,
            version=request.version,
            build_time=build_time
        )
        db.add(new_version)
        db.commit()

        return format_response(success=True, result={
            "environment": request.environment,
            "version": request.version,
            "build_time": build_time.strftime("%d/%m/%Y %H:%M:%S")
        })
    except Exception as e:
        db.rollback()
        return format_response(success=False, error=str(e))
