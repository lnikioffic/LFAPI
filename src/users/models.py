from typing import TYPE_CHECKING

from src.mixins import UserRelationMixin
from src.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from src.post.models import Post
    

class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)

    posts: Mapped[list['Post']] = relationship(back_populates='user')
    profile: Mapped['Profile'] = relationship(back_populates='user')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)


class Profile(Base, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = 'profile'

    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]

