from fastapi import FastAPI
from api import courses, sections, users
from db.db_table_setup import cli, init_models


def create_app() -> FastAPI:
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

    app.include_router(users.router)
    app.include_router(courses.router)
    app.include_router(sections.router)

    @app.on_event("startup")
    @cli.command()
    async def db_init_models():
        await init_models()

    return app