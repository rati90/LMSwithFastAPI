from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.services import auhontication
from db.models.user import User
from pydantic_schemas.user import UserInDB


async def get_user(db: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_user_by_email(db: AsyncSession, email: str):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_user_by_username(db: AsyncSession, username: str):
    query = select(User).where(User.username == username)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_user_by_id(db: AsyncSession, id: int):
    query = select(User).where(User.id == id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(User)
    result = await db.execute(query)
    return result.scalars().all()


async def create_user(db: AsyncSession, user: UserInDB):
    user.hashed_password = auhontication.get_password_hash(
        user.hashed_password
    )

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=user.hashed_password,
        role=user.role,
        is_active=user.is_active,
    )

    db.add(db_user)

    await db.commit()
    await db.refresh(db_user)

    return db_user
