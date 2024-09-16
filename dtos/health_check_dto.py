# from typing import Optional
#
#
# class HealthCheckDTO:
#     def __init__(self, status: str, version: Optional[str] = None, build_time: Optional[str] = None):
#         self.status = status
#         self.version = version
#         self.build_time = build_time or "Not available"  # Default to a human-readable string
#
#     def __repr__(self):
#         return f"HealthCheckDTO(status={self.status}, version={self.version}, build_time={self.build_time})"

from pydantic import BaseModel
from typing import Optional


class HealthCheckDTO(BaseModel):
    status: str
    version: Optional[str] = None
    build_time: Optional[str] = None
