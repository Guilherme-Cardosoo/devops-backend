from sqlalchemy.orm import Session

from app.models import Produto
from app.schemas import ProdutoCreate


def criar_produto(db: Session, produto: ProdutoCreate):
    novo_produto = Produto(
        nome=produto.nome,
        preco=produto.preco,
        categoria=produto.categoria
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto


def listar_produtos(db: Session):
    return db.query(Produto).all()


def buscar_produto(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()


def atualizar_produto(db: Session, produto_id: int, produto: ProdutoCreate):
    produto_db = buscar_produto(db, produto_id)

    if produto_db is None:
        return None

    produto_db.nome = produto.nome
    produto_db.preco = produto.preco
    produto_db.categoria = produto.categoria

    db.commit()
    db.refresh(produto_db)

    return produto_db


def excluir_produto(db: Session, produto_id: int):
    produto_db = buscar_produto(db, produto_id)

    if produto_db is None:
        return None

    db.delete(produto_db)
    db.commit()

    return produto_db