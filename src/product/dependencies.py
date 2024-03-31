from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.product.models import Product
from src.database import db
from src.product import service


async def product_by_id(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(db.scoped_sesion_dep),
) -> Product:
    product = await service.get_product(session=session, product_id=product_id)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found!",
    )