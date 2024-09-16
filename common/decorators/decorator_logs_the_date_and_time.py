from datetime import datetime
from functools import wraps


def log_datetime(func):
    """Log the date and time of a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Log the function name and time
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-" * 30}')
        # Pass along all arguments and keyword arguments
        return func(*args, **kwargs)

    return wrapper
