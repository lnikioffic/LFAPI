from typing import TYPE_CHECKING

from src.mixins import UserRelationMixin
from src.models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text


class Post(Base, UserRelationMixin):
    # _user_id_nullable = False
    # _user_id_unique = False
    _user_back_populates = 'posts'
    
    title: Mapped[str] = mapped_column(String(100), unique=False)
    body: Mapped[str] = mapped_column(Text, default='', server_default='')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, user_id={self.user_id})"

    def __repr__(self):
        return str(self)