from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post(
    "/produtos",
    response_model=schemas.ProdutoResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_produto(
    produto: schemas.ProdutoCreate,
    db: Session = Depends(get_db)
):
    return crud.criar_produto(db, produto)


@router.get(
    "/produtos",
    response_model=List[schemas.ProdutoResponse]
)
def listar_produtos(
    db: Session = Depends(get_db)
):
    return crud.listar_produtos(db)


@router.get(
    "/produtos/{produto_id}",
    response_model=schemas.ProdutoResponse
)
def buscar_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    produto = crud.buscar_produto(db, produto_id)

    if produto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )

    return produto


@router.put(
    "/produtos/{produto_id}",
    response_model=schemas.ProdutoResponse
)
def atualizar_produto(
    produto_id: int,
    produto: schemas.ProdutoCreate,
    db: Session = Depends(get_db)
):
    produto_atualizado = crud.atualizar_produto(db, produto_id, produto)

    if produto_atualizado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )

    return produto_atualizado


@router.delete(
    "/produtos/{produto_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def excluir_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    produto = crud.excluir_produto(db, produto_id)

    if produto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )

    crud.excluir_produto(db, produto_id)

    return