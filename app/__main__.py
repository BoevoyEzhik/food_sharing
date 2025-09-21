import uvicorn
from fastapi import FastAPI

from app.api.auth.auth_router import auth_router
from app.api.v1.v1_router import v1_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(v1_router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )
