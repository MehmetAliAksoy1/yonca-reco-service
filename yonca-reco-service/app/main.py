from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Yonca Data Service")
app.include_router(router, prefix="/api")
