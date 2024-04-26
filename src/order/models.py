from datetime import datetime
from typing import TYPE_CHECKING

from src.models import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import text, func, ForeignKey, UniqueConstraint

if TYPE_CHECKING:
    from src.product.models import Product


class Order(Base):
    promo: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )

    products: Mapped[list['Product']] = relationship(
        secondary='order_product',
        back_populates='orders'
    )

    # связь через ассоциативную модель
    products_details: Mapped[list['OrderProduct']] = relationship(
        back_populates='order'
    )

"""
если для связки нужны дополнительные данные то надо делать не через сквозную таблицу
а через ассоциативную модель
"""
class OrderProduct(Base):
    __tablename__ = 'order_product'
    __table_args__ = (UniqueConstraint('order_id', 'product_id', name='idx_unique'),)


    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    count: Mapped[int] = mapped_column(default=1, server_default='1')
    unit_price: Mapped[int] = mapped_column(default=0, server_default='0')

     # association between Assocation -> Order
    order: Mapped['Order'] = relationship(
        back_populates='products_details',
    )

    # association between Assocation -> Product
    product: Mapped['Product'] = relationship(
        back_populates='orders_details',
    )