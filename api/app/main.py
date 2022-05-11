from fastapi import FastAPI
import uvicorn
from app.core import config
from app.api.routers.networks import networks_router
from app.api.routers.localtest import localtest_router


app = FastAPI(
    title=config.PROJECT_NAME, docs_url="/docs", openapi_url="/"
)


@app.get("/hello")
async def root():
    return {"message": "Hello from " + config.PROJECT_NAME}

app.include_router(
    networks_router,
    prefix="/v1",
    tags=["networks"],
)

app.include_router(
    localtest_router,
    prefix="/v1",
    tags=["localtest"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
