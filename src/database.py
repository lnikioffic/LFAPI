from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker, 
    async_scoped_session, 
    AsyncSession)

from src.config import settings
from asyncio import current_task


class Database:
    def __init__(self, url: str, echo: bool = True):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session
    

    async def sesion_dep(self):
        async with self.session_factory() as session:
            yield session
            await session.close()


    async def scoped_sesion_dep(self):
        session = self.get_scoped_session()
        yield session
        await session.close()
    


db = Database(url=settings.db_url, echo=True)