from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProdutoBase(BaseModel):
    nome: str
    preco: Decimal
    categoria: str


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoUpdate(ProdutoBase):
    pass


class ProdutoResponse(ProdutoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)