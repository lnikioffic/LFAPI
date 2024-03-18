from fastapi import FastAPI
import uvicorn

from items.router import router as items_router
from users.router import router as users_route

app = FastAPI(title='main')
app.include_router(items_router)
app.include_router(users_route)


@app.get('/')
async def hello():
    return {'mess': 'Hello world'}



if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        reload=True
    )