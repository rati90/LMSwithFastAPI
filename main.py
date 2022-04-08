from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI LMS",
    description="Learning Management System",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


users = []


class User(BaseModel):
    email: str
    is_active: bool = True
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "User is saved"


@app.get('/users/{id}')
async def get_user(
        id: int = Path(..., description='The ID of the user you want to retrive', gt=0),
        q: str = Query(None, max_length=5)
        ):
    return { 'user': users[id], "query": q}

