from fastapi import FastAPI, Body
from pydantic import EmailStr

app = FastAPI()


@app.get('/')
async def hello():
    return {'mess': 'Hello world'}


@app.post('/user')
async def create_user(email: EmailStr = Body()):
    return {'mess': 'success', 'email': email}


@app.get('/items')
async def get_items():
    return {'mess': 'Hello world'}