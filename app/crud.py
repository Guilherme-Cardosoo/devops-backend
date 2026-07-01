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