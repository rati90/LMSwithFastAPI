from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = (
    "postgresql+asyncpg://postgres:password@localhost:5432/lms3"
)

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
)
#                              echo=True

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


Base = declarative_base()


async def async_get_db():
    async with async_session() as session:
        yield session
        await session.commit()
