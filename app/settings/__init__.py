from functools import lru_cache
from .base import Settings


def _get_settings():
    return Settings()


settings = _get_settings()
