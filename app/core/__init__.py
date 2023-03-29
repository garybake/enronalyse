from fastapi.templating import Jinja2Templates
from app.core.db import VDB   # noqa: F401

templates = Jinja2Templates(directory="templates")
