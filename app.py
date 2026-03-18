from fastapi import FastAPI
import csv
import os
from routes.clientes import router as clientes_router
from routes.ordens import router as ordens_router
from routes.produtos import router as produtos_router
from pydantic import BaseModel

app = FastAPI()

app.include_router(clientes_router)
app.include_router(produtos_router)
app.include_router(ordens_router)

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


file_clientes = './routes/Clientes.csv'
file_produtos = './routes/Produtos.csv'
file_ordens = './routes/OrdemDeVendas.csv'

# ----------------- INICIALIZAÇÃO DOS ARQUIVOS CSV -----------------
if not os.path.exists(file_clientes):
    with open(file_clientes, mode='w', newline='', encoding='utf-8') as file:
        data = [["ID", "NOME", "SOBRENOME", "DATA_NASCIMENTO", "CPF"]]
        writer = csv.writer(file)
        writer.writerows(data)


if not os.path.exists(file_produtos):
    with open(file_produtos, mode='w', newline='', encoding='utf-8') as file:
        data = [["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]]
        writer = csv.writer(file)
        writer.writerows(data)

if not os.path.exists(file_ordens):
    with open(file_ordens, mode='w', newline='', encoding='utf-8') as file:
        data = [["ID", "CLIENTE_ID", "PRODUTO_ID"]]
        writer = csv.writer(file)
        writer.writerows(data)