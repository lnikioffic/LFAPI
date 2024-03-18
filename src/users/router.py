from typing import Annotated
from fastapi import Path, APIRouter
from users.shemas import CreateUser
from users import service


router = APIRouter(prefix='/users', tags=['Users'])


@router.post('')
async def create_user(user: CreateUser):
    return await service.create_user(user)