from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="DevOps Backend",
    version="1.0.0",
    description="API para gerenciamento de produtos."
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "API funcionando!"}