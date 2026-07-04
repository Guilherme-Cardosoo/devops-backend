from fastapi import FastAPI

from app.database import Base, engine
from app.models import Produto
from app.routes import router

# Cria todas as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DevOps Backend",
    version="1.0.0",
    description="API para gerenciamento de produtos."
)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "API funcionando!"}