from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.product.router import router as items_router
from src.users.router import router as users_router
from src.auth.router import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title='main', lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(auth_router)


@app.get('/')
async def hello():
    return {'mess': 'Hello world'}