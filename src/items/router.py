from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Path, APIRouter, HTTPException, status, Depends

from src.database import db
from src.items.shemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial
from src.items import service
from src.items.dependencies import product_by_id

router = APIRouter(prefix='/items', tags=['Items'])


@router.get('', response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db.scoped_sesion_dep)):
    return await service.get_products(session=session)


@router.get('/{product_id}', response_model=Product)
async def get_product(product: Product = Depends(product_by_id)):
    return product


@router.post('', response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, 
                         session: AsyncSession = Depends(db.scoped_sesion_dep)):
    pr = await service.create_product(session=session, product=product)
    if pr is not None:
        return pr
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'not found'
    )


@router.put("/{product_id}/")
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db.scoped_sesion_dep),
):
    return await service.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.patch("/{product_id}/")
async def update_product_partial(
    product_update: ProductUpdatePartial,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db.scoped_sesion_dep),
):
    return await service.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True,
    )


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db.scoped_sesion_dep),
) -> None:
    await service.delete_product(session=session, product=product)