from dependency_injector import containers, providers
from .clients.redis import RedisClient
from app.settings import settings


class CacheAdapter(containers.DeclarativeContainer):
    redis_adapter = providers.Resource(
        RedisClient.init_redis_pool, host=settings.cache_host
    )
