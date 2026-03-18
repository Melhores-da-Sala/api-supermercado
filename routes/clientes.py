from fastapi import APIRouter
from pydantic import BaseModel
import csv
import os

router = APIRouter()

caminho_arquivo = "./routes/Clientes.csv"

class Cliente(BaseModel):
    nome: str
    sobrenome: str
    data_nascimento: str
    cpf: str

arquivo_id_clientes = './routes/arquivo_id.txt'
def gerar_id():
    # arquivo de controle de id
    if not os.path.exists(arquivo_id_clientes):
        with open(arquivo_id_clientes, 'w') as f:
            f.write("0")
    
    with open(arquivo_id_clientes, 'r') as f:
        ultimo_id = int(f.read().strip()) # usamos o strip para remover os espacos no final
    
    novo_id = ultimo_id + 1
    
    with open(arquivo_id_clientes, 'w') as f:
        f.write(str(novo_id))
        
    return novo_id



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
@router.post("/clientes")
async def criar_cliente(cliente: Cliente):
    data = [["ID", "NOME", "SOBRENOME", "DATA_NASCIMENTO", "CPF"]]
    cpf_enviado = cliente.cpf.strip()

    with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or row[0] == "ID":
                continue
            
            if row[4].strip() == cpf_enviado:
                return {"ERRO": "Este CPF já está cadastrado!"}
            
            data.append(row)
    
    novo_id = gerar_id()
    
    data.append([novo_id, cliente.nome, cliente.sobrenome, cliente.data_nascimento, cliente.cpf])

    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    return {"mensagem": "Cliente adicionado com sucesso", "id": novo_id}


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