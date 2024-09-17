from typing import Optional, Any
from pydantic import BaseModel


class ResponseDTO(BaseModel):
    success: bool
    error: Optional[str] = None
    result: Optional[Any] = None
    paging: Optional[Any] = None
