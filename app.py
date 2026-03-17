from fastapi import FastAPI
from routes.clientes import router as clientes_router
from pydantic import BaseModel

app = FastAPI()

app.include_router(clientes_router)


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


file_clientes = 'Clientes.csv'
file_produtos = 'Produtos.csv'
file_ordens = 'OrdemDeVendas.csv'
