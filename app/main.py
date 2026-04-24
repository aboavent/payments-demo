from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import APP_TITLE, APP_VERSION
from app.routes import router

app = FastAPI(title=APP_TITLE, version=APP_VERSION)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)
