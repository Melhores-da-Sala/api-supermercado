from fastapi import APIRouter
import os
import csv
from pydantic import BaseModel

router = APIRouter()

caminho_arquivo = "OrdemDeVendas.csv"


# cria o arquivo se não existir
if not os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        dados = [
            ["ID", "ID_CLIENTE", "ID_PRODUTO"]
        ]
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)
else:
    print("O arquivo já existe!")


class OrdemDeVenda(BaseModel):
    id: int
    cliente_id: int
    produto_id: int


# LISTAR TODAS
@router.get("/ordens_de_venda")
def ordens_de_venda():

    ordens = []

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue
            else:
                ordens.append({
                    "id": linha[0],
                    "cliente_id": linha[1],
                    "produto_id": linha[2]
                })

    return ordens


# BUSCAR POR ID
@router.get("/ordens_de_venda/{ordem_id}")
def buscar_ordem(ordem_id: str):

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == ordem_id:
                return {
                    "id": linha[0],
                    "cliente_id": linha[1],
                    "produto_id": linha[2]
                }

    return {"ERRO": "ID não localizado"}


# ADICIONAR
@router.post("/add_ordem_de_venda")
async def adicionar_ordem(ordem: OrdemDeVenda):

    dados = [
        ["ID", "ID_CLIENTE", "ID_PRODUTO"]
    ]

    ordens = []

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue
            else:
                dados.append(linha)

    nova_ordem = [ordem.id, ordem.cliente_id, ordem.produto_id]
    dados.append(nova_ordem)

    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue
            else:
                ordens.append({
                    "id": linha[0],
                    "cliente_id": linha[1],
                    "produto_id": linha[2]
                })

    return ordens


# DELETAR
@router.delete("/del_ordem_de_venda/{ordem_id}")
def deletar_ordem(ordem_id: str):

    dados = [
        ["ID", "ID_CLIENTE", "ID_PRODUTO"]
    ]

    ordens = []

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue
            else:
                dados.append(linha)

    status = False

    for linha in dados:
        if linha[0] == ordem_id:
            dados.pop(dados.index(linha))
            status = True

    if status != True:
        return {"ERRO": "ID informado não existe"}

    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue
            else:
                ordens.append({
                    "id": linha[0],
                    "cliente_id": linha[1],
                    "produto_id": linha[2]
                })

    return ordens


# EDITAR
@router.put("/edit_ordem_de_venda")
async def editar_ordem(ordem: OrdemDeVenda):

    dados = [
        ["ID", "ID_CLIENTE", "ID_PRODUTO"]
    ]

    ordens = []

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue
            else:
                dados.append(linha)

    status = False

    for linha in dados:
        if linha[0] == str(ordem.id):
            linha[1] = ordem.cliente_id
            linha[2] = ordem.produto_id
            status = True

    if status != True:
        return {"ERRO": "ID informado não existe"}

    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue
            else:
                ordens.append({
                    "id": linha[0],
                    "cliente_id": linha[1],
                    "produto_id": linha[2]
                })

    return ordens