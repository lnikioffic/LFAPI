from src.models import Base
from src.order.models import Order
from sqlalchemy.orm import Mapped, relationship


class Product(Base):
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]

    orders: Mapped[list['Order']] = relationship (
        secondary='order_product',
        back_populates='products'
    )

