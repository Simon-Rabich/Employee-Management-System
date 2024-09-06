from pydantic import BaseModel


class HealthCheckDTO(BaseModel):
    status: str
    version: str = None
    buildTime: str = None
