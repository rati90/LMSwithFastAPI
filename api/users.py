from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import get_db
from pydantic_schemas.user import UserCreate, User
from pydantic_schemas.courses import Course
from api.utils.users import get_users, get_user, get_user_by_email, create_user
from api.utils.courses import get_user_courses

router = APIRouter(
    prefix="/users",
    tags=["USERS"],
    responses={404: {"description": "Not found"}},
)


@router.get("/all", response_model=list[User])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    users = await get_users(db, skip=skip, limit=limit)
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return users


@router.post(
    "/create", response_model=User, status_code=status.HTTP_201_CREATED
)
async def create_new_user(
    user: UserCreate, db: AsyncSession = Depends(get_db)
):
    db_user = await get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with this {db_user.email} email Already created",
        )

    return await create_user(db=db, user=user)


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return db_user


@router.get("/{user_id}/courses", response_model=list[Course])
async def read_user_courses(user_id: int, db: AsyncSession = Depends(get_db)):
    courses = await get_user_courses(user_id=user_id, db=db)
    if courses is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return courses
