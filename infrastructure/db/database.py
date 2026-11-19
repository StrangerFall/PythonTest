from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.infrastructure.config import settings

async_engine = create_async_engine(
    url= settings.get_url()
)
session_factory = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

async def get_async_session():
    async with session_factory() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_async_session)]
