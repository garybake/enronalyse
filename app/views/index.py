from typing import Any

from fastapi import APIRouter
from fastapi import Request

from app.core import templates

router = APIRouter()


@router.get("/")
async def render_index(request: Request) -> Any:
    return templates.TemplateResponse("index.html", {"request": request})
