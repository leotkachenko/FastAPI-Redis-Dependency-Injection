import logging
from fastapi import Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide

from ..services.cache.service import CacheService
from ..containers import Container


@inject
async def cache(
    cache_provider: CacheService = Depends(Provide[Container.cache_service]),
) -> CacheService:
    try:
        return cache_provider
    except Exception as error:
        logging.error(f"Cache Service {error=}")
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
