from fastapi import APIRouter
from pydantic import BaseModel
import csv

router = APIRouter()


# Modelo da ordem de venda
class OrdemDeVenda(BaseModel):
    id: int
    cliente_id: int
    produto_id: int


arquivo_ordens = './routes/OrdemDeVendas.csv'


# Retorna todas as ordens de venda
@router.get("/ordens_de_venda")
def ordens_de_venda():

    ordens = []

    with open(arquivo_ordens, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue

            ordens.append({
                "id": linha[0],
                "id_cliente": linha[1],
                "id_produto": linha[2]
            })

    if not ordens:
        return {"aviso": "Nenhuma ordem de venda"}

    return ordens


# Adiciona uma nova ordem de venda
@router.post("/add_cliente")
async def add_cliente(ordem: OrdemDeVenda):

    ordens = []

    # Lê as ordens existentes
    with open(arquivo_ordens, mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == 'ID':
                continue
            ordens.append(linha)

    # Adiciona a nova ordem
    novo = [str(ordem.id), str(ordem.cliente_id), str(ordem.produto_id)]
    ordens.append(novo)

    # Salva todas as ordens no CSV
    with open(arquivo_ordens, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["ID", "ID_CLIENTE", "ID_PRODUTO"])
        escritor.writerows(ordens)

    return ordens



@router.delete("/del_cliente/{cliente_id}")
def del_cliente(cliente_id: int):

    ordens = []

    with open(arquivo_ordens, mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[0] == 'ID':
                continue
            ordens.append(linha)

    # Separa as ordens que NÃO têm o ID informado
    ordens_filtradas = [linha for linha in ordens if linha[0] != str(cliente_id)]

    if len(ordens_filtradas) == len(ordens):
        return {"ERRO": "ID informado não existe"}

    with open(arquivo_ordens, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["ID", "ID_CLIENTE", "ID_PRODUTO"])
        escritor.writerows(ordens_filtradas)

    return ordens_filtradas