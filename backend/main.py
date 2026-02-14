from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.database.db import create_db_and_tables
from backend.routes.usuario_routes import router as usuario_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables() 
    yield

app = FastAPI(
    lifespan=lifespan,
    title="API Fit",
    version="1.0.0")

@app.get("/")
def root():
    return {"status": "API rodando"}
app.include_router(usuario_router)