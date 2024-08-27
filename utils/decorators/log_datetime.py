from datetime import datetime
from functools import wraps
from typing import Callable


# decorator_logs_the_date_and_time

def log_datetime(func: Callable) -> Callable:
    """Log the date and time of a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-" * 30}')
        return func(*args, **kwargs)

    return wrapper


@log_datetime
def daily_backup():
    print('Daily backup job has finished.')


if __name__ == '__main__':
    daily_backup()
