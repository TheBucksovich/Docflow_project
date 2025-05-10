from fastapi import FastAPI

from app.utils.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
)
