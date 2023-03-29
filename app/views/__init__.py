from fastapi import APIRouter

from app.views import index

view_router = APIRouter()
view_router.include_router(index.router, prefix="/pages", tags=["pages"])
