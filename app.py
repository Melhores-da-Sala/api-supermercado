from fastapi import FastAPI
import os
import csv
from pydantic import BaseModel
from routes import produtos

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


file_clientes = 'Clientes.csv'
file_produtos = 'Produtos.csv'
file_ordens = 'OrdemDeVendas.csv'

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

app.include_router(produtos.router)