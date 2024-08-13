from typing import Optional, Any
from pydantic import BaseModel
from dataclasses import dataclass


# @dataclass()
class ResponseDTO(BaseModel):
    success: bool
    error: Optional[str] = None
    result: Optional[Any] = None
    paging: Optional[Any] = None
