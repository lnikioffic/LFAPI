from src.models import Base
from src.order.models import Order, OrderProduct
from sqlalchemy.orm import Mapped, relationship


class Product(Base):
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]

    orders: Mapped[list['Order']] = relationship (
        secondary='order_product',
        back_populates='products'
    )

    # связь через ассоциативную модель
    orders_details: Mapped[list['OrderProduct']] = relationship(
        back_populates='product'
    )


