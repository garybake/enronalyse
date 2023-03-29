from typing import Any

from fastapi import APIRouter, Form

from app.models import Email

router = APIRouter()


@router.post("/v_search")
async def post_v_search(searchTerm: str = Form(), searchRowCount: str = Form()) -> Any:
    """
    Do search query
    """
    print(searchTerm)
    row_count = int(searchRowCount)
    em = Email()
    res = em.get_emails(concepts=searchTerm, row_count=row_count)

    return res
