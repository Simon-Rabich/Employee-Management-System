from typing import Optional, Any

from dtos.response_dto import ResponseDTO


def format_response(success: bool, result: Optional[Any] = None, error: Optional[str] = None,
                    paging: Optional[Any] = None) -> ResponseDTO:
    return ResponseDTO(success=success, error=error, result=result, paging=paging)