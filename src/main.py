from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.items.router import router as items_router
from src.users.router import router as users_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title='main', lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_route)


@app.get('/')
async def hello():
    return {'mess': 'Hello world'}