from fastapi import FastAPI
from routes.ordens import router as ordens_router
from pydantic import BaseModel


class Cliente(BaseModel):
    id: int
    nome: str
    sobrenome: str
    data_nascimento: str
    cpf: str


class Produto(BaseModel):
    id: int
    nome: str
    fornecedor: str
    quantidade: int


class OrdemDeVenda(BaseModel):
    id: int
    cliente_id: int
    produto_id: int


app = FastAPI()
app.include_router(ordens_router)

file_clientes = "./routes/Clientes.csv"
file_produtos = "./routes/Produtos.csv"
