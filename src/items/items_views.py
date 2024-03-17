from typing import Annotated
from fastapi import Path, APIRouter


router = APIRouter(prefix='/items', tags=['Items'])


@router.get('')
async def get_items():
    return {'mess': 'Hello world'}


@router.get('/latest')
async def get_item_latest():
    return {'item': {'id': 0}}


@router.get('/{item_id}')
async def get_items(item_id: Annotated[int, Path(ge=1, lt=1000000)]):
    return {'item': {'id': item_id}}