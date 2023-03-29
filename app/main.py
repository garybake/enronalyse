from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.views import view_router
from app.api.v1 import api_router

app = FastAPI(title="Enronalyse")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(view_router)
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    response = RedirectResponse(url="/pages")
    return response
