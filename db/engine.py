from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase  # ← додай імпорт

from core.config import settings


engine = create_async_engine(settings.DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):  # ← додай Base
    pass


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


CurrentSession = Annotated[AsyncSession, Depends(get_db)]
