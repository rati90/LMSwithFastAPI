from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_setup import async_get_db
from pydantic_schemas.courses import Course, CourseCreate
from api.utils.courses import get_courses, get_course, create_course

router = APIRouter(
    prefix="/courses",
    tags=["COURSES"],
    responses={404: {"description": "Not found"}},
)


@router.get("/all", response_model=list[Course])
async def read_courses(db: AsyncSession = Depends(async_get_db)):
    courses = await get_courses(db=db)
    if courses is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return courses


@router.post(
    "/create", response_model=Course, status_code=status.HTTP_201_CREATED
)
async def create_new_course(
    course: CourseCreate, db: AsyncSession = Depends(async_get_db)
):
    return await create_course(db=db, course=course)


@router.get("/{course_id}")
async def read_course(
    course_id: int, db: AsyncSession = Depends(async_get_db)
):
    db_course = await get_course(db=db, course_id=course_id)

    if db_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return db_course


@router.patch("/courses/{course_id}")
async def update_course():
    return {"courses": []}


@router.delete("/courses/{course_id}")
async def delete_course():
    return {"courses": []}
