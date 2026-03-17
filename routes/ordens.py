from fastapi import APIRouter
import os
import csv
from pydantic import BaseModel

router = APIRouter()

caminho_arquivo = "OrdemDeVendas.csv"


# =========================
# CRIA ARQUIVO SE NÃO EXISTIR
# =========================
if not os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["ID_ORDEM", "ID_CLIENTE", "ID_PRODUTO"])


# =========================
# MODEL
# =========================
class OrdemDeVenda(BaseModel):
    cliente_id: int
    produto_id: int


# =========================
# GERAR ID ÚNICO
# =========================
def gerar_id():
    ids = []

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID_ORDEM":
                continue
            ids.append(int(linha[0]))

    if not ids:
        return 1

    return max(ids) + 1


# =========================
# LISTAR TODAS
# =========================
@router.get("/ordens_de_venda")
def ordens_de_venda():
    ordens = []

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID_ORDEM":
                continue

            ordens.append({
                "id": int(linha[0]),
                "cliente_id": int(linha[1]),
                "produto_id": int(linha[2])
            })

    return ordens


# =========================
# BUSCAR POR ID
# =========================
@router.get("/ordens_de_venda/{ordem_id}")
def buscar_ordem(ordem_id: int):

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID_ORDEM":
                continue

            if int(linha[0]) == ordem_id:
                return {
                    "id": int(linha[0]),
                    "cliente_id": int(linha[1]),
                    "produto_id": int(linha[2])
                }

    return {"erro": "ID não localizado"}


# =========================
# ADICIONAR
# =========================
@router.post("/add_ordem_de_venda")
async def adicionar_ordem(ordem: OrdemDeVenda):

    dados = [["ID_ORDEM", "ID_CLIENTE", "ID_PRODUTO"]]

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID_ORDEM":
                continue
            dados.append(linha)

    novo_id = gerar_id()
    nova_ordem = [novo_id, ordem.cliente_id, ordem.produto_id]
    dados.append(nova_ordem)

    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

    return {
        "msg": "Ordem criada com sucesso",
        "id": novo_id
    }


# =========================
# DELETAR
# =========================
@router.delete("/del_ordem_de_venda/{ordem_id}")
def deletar_ordem(ordem_id: int):

    dados = [["ID_ORDEM", "ID_CLIENTE", "ID_PRODUTO"]]
    status = False

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID_ORDEM":
                continue

            if int(linha[0]) == ordem_id:
                status = True
                continue

            dados.append(linha)

    if not status:
        return {"erro": "ID informado não existe"}

    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

    return {"msg": "Ordem deletada com sucesso"}


# =========================
# EDITAR
# =========================
@router.put("/edit_ordem_de_venda/{ordem_id}")
async def editar_ordem(ordem_id: int, ordem: OrdemDeVenda):

    dados = [["ID_ORDEM", "ID_CLIENTE", "ID_PRODUTO"]]
    status = False

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID_ORDEM":
                continue

            if int(linha[0]) == ordem_id:
                dados.append([ordem_id, ordem.cliente_id, ordem.produto_id])
                status = True
            else:
                dados.append(linha)

    if not status:
        return {"erro": "ID informado não existe"}

    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

    return {"msg": "Ordem atualizada com sucesso"}