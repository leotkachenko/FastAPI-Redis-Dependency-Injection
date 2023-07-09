import uvicorn
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api as api_v1
from app.settings import settings
from app import container


def get_app() -> FastAPI:
    server = FastAPI(
        tittle=settings.app_name,
        openapi_url=settings.openapi_route,
    )
    server.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    server.container = container
    server.include_router(
        api_v1.router,
        prefix=settings.api_v1_route,
    )
    return server


app = get_app()


@app.get("/healthcheck")
async def healthcheck() -> Response:
    return Response()


def main():
    uvicorn.run(
        "app.main:app", host="0.0.0.0", port=8080, log_level="info", reload=True
    )


if __name__ == "__main__":
    main()
