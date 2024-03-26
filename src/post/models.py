from typing import TYPE_CHECKING

from src.mixins import UserRelationMixin
from src.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey

if TYPE_CHECKING:
    from src.users.models import User


class Post(Base, UserRelationMixin):
    # _user_id_nullable = False
    # _user_id_unique = False
    _user_back_populates = 'posts'
    
    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(Text, default='', server_default='')
