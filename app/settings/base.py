from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastApi + Redis + Dependency Injection"
    api_v1_route: str = "/api/v1"
    openapi_route: str = "/api/v1/openapi.json"
    cache_host: str = "redis_cache"
    origins: list[str] = ["http://localhost:3000", "http://localhost:8080"]
