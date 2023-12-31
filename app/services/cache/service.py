import json
from redis.asyncio import Redis


class CacheService:
    def __init__(self, provider: Redis) -> None:
        self.__provider = provider

    async def get(self, key):
        value = await self.__provider.get(str(key))
        return json.loads(value) if value else None

    async def set(self, key, value, exp=None):
        return await self.__provider.set(str(key), value, exp)

    async def delete(self, key):
        return await self.__provider.delete(str(key))

    async def get_all(self):
        keys = await self.__provider.keys("*")
        return [json.loads(await self.__provider.get(key)) for key in keys]
