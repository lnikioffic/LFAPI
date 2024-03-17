from fastapi import FastAPI, Body, Path
from pydantic import EmailStr
from typing import Annotated
import uvicorn

from items.items_views import router as items_router

app = FastAPI(title='main')
app.include_router(items_router)


@app.get('/')
async def hello():
    return {'mess': 'Hello world'}


@app.post('/user')
async def create_user(email: EmailStr = Body()):
    return {'mess': 'success', 'email': email}


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        reload=True
    )