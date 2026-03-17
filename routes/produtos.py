from fastapi import APIRouter
from pydantic import BaseModel
import csv

router = APIRouter()
file_produtos = 'Produtos.csv'

class Produto(BaseModel):
    nome: str
    fornecedor: str
    quantidade: int

################################### GET ######################################
@router.get("/produtos")
def listar_produtos():
    produtos_dict = {}

    with open(file_produtos, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or row[0] == "ID":
                continue
            
            id_produto = row[0] 
            produtos_dict[id_produto] = {
                "nome": row[1],
                "fornecedor": row[2],
                "quantidade": int(row[3])
            }

    return produtos_dict

################################### POST ####################################
@router.post("/produtos")
async def criar_produtos(produto: Produto):
    data = [["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]]
    novo_id = 1  

    with open(file_produtos, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or row[0] == "ID":
                continue
            
            data.append(row)
            novo_id = int(row[0]) + 1
    
    data.append([novo_id, produto.nome, produto.fornecedor, produto.quantidade])

    with open(file_produtos, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return {"mensagem": "Produto adicionado com sucesso"}

################################### PUT #######################################
@router.put("/produtos/{produto_id}")
async def atualizar_dados(produto_id: int, produto: Produto):
    data = [["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]]
    atualizou = False

    with open(file_produtos, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or row[0] == "ID":
                continue
            
            if int(row[0]) == produto_id:
                data.append([produto_id, produto.nome, produto.fornecedor, produto.quantidade])
                atualizou = True
            else:
                data.append(row)

    if not atualizou:
        return {"ERRO": "ID informado não existe"}

    with open(file_produtos, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return {"mensagem": f"Produto {produto_id} atualizado!"}

############################## DELETE ########################################
@router.delete("/produtos/{produto_id}")
def del_produto(produto_id: int):
    data = [["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]]
    deletou = False

    with open(file_produtos, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or row[0] == "ID":
                continue
            
            if int(row[0]) == produto_id:
                deletou = True
            else:
                data.append(row)

    if not deletou:
        return {"ERRO": "ID informado não existe"}

    with open(file_produtos, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return {"mensagem": f"Produto {produto_id} deletado com sucesso!"}