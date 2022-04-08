from fastapi import APIRouter

router = APIRouter()


@router.get("/section/{id}")
async def read_section():
    return {"courses": []}


@router.get("/section/:id/content-blocks")
async def read_section_content_blocks():
    return {"courses": []}


@router.get("/content-blocks/{id}")
async def read_content_block():
    return {"courses": []}

