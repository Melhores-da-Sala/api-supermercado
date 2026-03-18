from fastapi import APIRouter
import os
import csv
from pydantic import BaseModel

router = APIRouter()

caminho_arquivo = "./routes/OrdemDeVendas.csv"


# =========================
# CRIA ARQUIVO SE NÃO EXISTIR
# =========================
if not os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["ID", "CLIENTE_ID", "PRODUTO_ID"])


# =========================
# MODEL
# =========================
class OrdemDeVenda(BaseModel):
    cliente_id: int
    produto_id: int


# =========================
# GERAR ID ÚNICO
# =========================
arquivo_id_ordens = './routes/arquivo_id.txt'
def gerar_id():
    # arquivo de controle de id
    if not os.path.exists(arquivo_id_ordens):
        with open(arquivo_id_ordens, 'w') as f:
            f.write("0")
    
    with open(arquivo_id_ordens, 'r') as f:
        ultimo_id = int(f.read().strip()) # usamos o strip para remover os espacos no final
    
    novo_id = ultimo_id + 1
    
    with open(arquivo_id_ordens, 'w') as f:
        f.write(str(novo_id))
        
    return novo_id


# =========================
# LISTAR TODAS
# =========================
@router.get("/ordens_de_venda")
def ordens_de_venda():
    ordens = []
    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if not linha or not linha[0].isdigit(): # BLINDAGEM: Se a linha for vazia ou o primeiro item não for número, pule.
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
            if not linha or not linha[0].isdigit():
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
    dados = [["ID", "CLIENTE_ID", "PRODUTO_ID"]]
    
    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if not linha or not linha[0].isdigit(): # BLINDAGEM
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
    dados = [["ID", "CLIENTE_ID", "PRODUTO_ID"]]
    status = False

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if not linha or not linha[0].isdigit(): # BLINDAGEM
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
    dados = [["ID", "CLIENTE_ID", "PRODUTO_ID"]]
    status = False

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if not linha or not linha[0].isdigit(): # BLINDAGEM
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