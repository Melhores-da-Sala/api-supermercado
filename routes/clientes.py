from fastapi import APIRouter
from pydantic import BaseModel
import csv
import os

router = APIRouter()

caminho_arquivo = "./routes/Clientes.csv"

class Cliente(BaseModel):
    id: int
    nome: str
    sobrenome: str
    data_nascimento: str
    cpf: str
    
def gerar_id():
    ids = []

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue
            ids.append(int(linha[0]))

    if not ids:
        return 1

    return max(ids) + 1



@router.get("/listar_clientes")
def listar_clientes():
    clientes = []

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue

            clientes.append({
                "id": int(linha[0]),
                "nome": linha[1],
                "sobrenome": linha[2],
                "data_nascimento": linha[3],
                "cpf": linha[4]
            })

    return clientes


@router.get("/listar_clientes/{cliente_id}")
def buscar_cliente(cliente_id: int):

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue

            if int(linha[0]) == cliente_id:
                return {
                    "id": int(linha[0]),
                    "nome": linha[1],
                    "sobrenome": linha[2],
                    "data_nascimento": linha[3],
                    "cpf": linha[4]
                }

    return {"erro": "Cliente não encontrado"}



@router.post("/add_clientes")
async def criar_cliente(cliente: Cliente):

    dados = [["ID", "NOME", "SOBRENOME", "DATA_NASCIMENTO", "CPF"]]

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue
            dados.append(linha)

    novo_id = gerar_id()
    dados.append([novo_id, cliente.nome, cliente.sobrenome, cliente.data_nascimento, cliente.cpf])

    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

    return {
        "mensagem": "Cliente registrado com sucesso",
        "id": novo_id
    }


@router.put("/update_clientes/{cliente_id}")
async def atualizar_cliente(cliente_id: int, cliente: Cliente):

    dados = [["ID", "NOME", "SOBRENOME", "DATA_NASCIMENTO", "CPF"]]
    encontrado = False

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue

            if int(linha[0]) == cliente_id:
                dados.append([cliente_id, cliente.nome, cliente.sobrenome, cliente.data_nascimento, cliente.cpf])
                encontrado = True
            else:
                dados.append(linha)

    if not encontrado:
        return {"erro": "Cliente não encontrado"}

    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

    return {"mensagem": "Cliente atualizado com sucesso"}



@router.delete("/delete_clientes/{cliente_id}")
def deletar_cliente(cliente_id: int):

    dados = [["ID", "NOME", "SOBRENOME", "DATA_NASCIMENTO", "CPF"]]
    encontrado = False

    with open(caminho_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == "ID":
                continue

            if int(linha[0]) == cliente_id:
                encontrado = True
                continue

            dados.append(linha)

    if not encontrado:
        return {"erro": "Cliente não encontrado"}

    with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

    return {"mensagem": "Cliente deletado com sucesso"}