from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://postgres:password@localhost:5432/lms3"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)

# Async connection to db

ASYNC_SQLALCHEMY_DATABASE_URL = (
    "postgresql+asyncpg://postgres:password@localhost:5432/lms3"
)

async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)

Async_SessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def async_get_db():
    async with Async_SessionLocal() as db:
        yield db
        await db.commit()
