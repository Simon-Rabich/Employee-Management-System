from common.configurations.config import DATABASE_URL


def get_config() -> dict:
    config: dict = DATABASE_URL
    return config
