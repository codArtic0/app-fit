from fastapi import FastAPI
from backend.routes.usuario_routes import router as usuario_router

app = FastAPI(
    title="API Fit",
    version="1.0.0"
)

# Health check
@app.get("/")
def root():
    return {"status": "API rodando"}

# Registrar rotas
app.include_router(usuario_router)