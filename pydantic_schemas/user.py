from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    email: str
    role: int = 2
    is_active: bool = True


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

