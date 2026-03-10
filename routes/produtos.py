from pydantic import BaseModel
import csv
from fastapi import APIRouter

class Produto(BaseModel):
    nome: str
    fornecedor: str
    quantidade: int

file_produtos = 'Produtos.csv'

router = APIRouter()

#################################### GET #####################################
@router.get("/produtos")
def listar_produtos():
    lista_produtos = []

    with open(file_produtos, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "ID":
                continue

            produto = {
                "id": int(row[0]),
                "nome": row[1],
                "fornecedor": row[2],
                "quantidade": int(row[3])
            }

            lista_produtos.append(produto)

    return lista_produtos
##############################################################################
################################### POST #####################################
@router.post("/produtos")
async def criar_produtos(produto: Produto):

    data = [["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]]
    id = 0

    with open(file_produtos, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == 'ID':
                continue
            data.append(row)
            id = max(id, int(row[0]))
    
    novo_id = id + 1

    data.append([novo_id, produto.nome, produto.fornecedor, produto.quantidade])

    with open(file_produtos, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return {"mensagem": "Produto adicionado"}
##############################################################################
################################### DELETE ###################################
@router.delete("/produtos/{produto_id}")
def del_produto(produto_id:int):
    data = [
        ["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]
    ]
    
    Produto = {}

    with open(file_produtos, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                data.append(row)
    
    cont = False
    for linha in data:
        if linha[0] == produto_id:
            data.pop(data.index(linha))
            cont = True

    if cont != True:
        return {"ERRO":"ID informado não existe"}        
    
    with open(file_produtos, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    with open(file_produtos, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                Produto[row[0]] = row[1]

    return Produto
##############################################################################
#################################### PUT #####################################
@router.put("/produtos")
async def atualizar_dados(produto: Produto):

    data = [["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]]

    Produto = {}

    with open(file_produtos, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or row[0] == 'ID':
                continue
            else:
                data.append(row)

    cont = False
    for linha in data:
        if linha[0] == str(produto.id):
            linha[1] = produto.nome
            linha[2] = produto.fornecedor
            linha[3] = str(produto.quantidade)
            cont = True

    if cont != True:
        return {"ERRO":"ID informado não existe"}   
          
    with open(file_produtos, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_produtos, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                Produto[row[0]] = row[1]

    return Produto
##############################################################################