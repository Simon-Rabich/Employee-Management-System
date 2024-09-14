from datetime import datetime

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.models.product_version import ProductVersion
from dtos.response_dto import ResponseDTO
from utils.format_response import format_response

router = APIRouter()


@router.post("/product_version", response_model=ResponseDTO)
def add_product_version(
        environment: str = Query(...),
        version: str = Query(...),
        build_time: datetime = Query(...),
        db: Session = Depends(get_db)
) -> ResponseDTO:
    try:
        new_version = ProductVersion(environment=environment, version=version, build_time=build_time)
        db.add(new_version)
        db.commit()
        return format_response(success=True,
                               result={"environment": environment, "version": version, "build_time": build_time})
    except Exception as e:
        db.rollback()
        return format_response(success=False, error=str(e))