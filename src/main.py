from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.models import Base
from src.items.models import *
from src.database import db

import uvicorn

from src.items.router import router as items_router
from src.users.router import router as users_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield



app = FastAPI(title='main', lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_route)


@app.get('/')
async def hello():
    return {'mess': 'Hello world'}


if __name__ == '__main__':
    pass
    # uvicorn.run(
    #     app='main:app',
    #     reload=True
    # )