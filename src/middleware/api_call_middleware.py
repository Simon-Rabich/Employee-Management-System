from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from src.metrics import USAGE_API_CALLS


class APICallMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Increment the counter for each API call
        USAGE_API_CALLS.inc()

        response = await call_next(request)
        return response
