from pydantic import BaseModel
from typing import Optional


class HealthCheckDTO(BaseModel):
    status: str
    version: Optional[str] = None
    build_time: Optional[str] = None
