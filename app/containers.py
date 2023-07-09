from dependency_injector import containers, providers

from .services.cache import cache_adapter
from .services.cache.service import CacheService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.api.dependecies"])
    cache_service = providers.Factory(
        CacheService, provider=cache_adapter.redis_adapter
    )
