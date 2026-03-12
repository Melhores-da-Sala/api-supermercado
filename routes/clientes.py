from fastapi import APIRouter
from pydantic import BaseModel
import csv

router = APIRouter()

class Cliente(BaseModel):
    id: int
    nome: str
    sobrenome: str
    data_nascimento: str
    cpf: str

file_clientes = './routes/Clientes.csv'

@router.get("/listar_clientes")
def listar_clientes():
    clientes = []

    with open(file_clientes, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            if len(row) < 5:
                continue

            clientes.append({
                "id": int(row[0]),
                "nome": row[1],
                "sobrenome": row[2],
                "data_nascimento": row[3],
                "cpf": row[4]
            })

    return clientes


@router.post("/add_clientes")
def criar_cliente(cliente: Cliente):
    with open(file_clientes, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            if not row or len(row) < 2:
                continue

            if int(row[0]) == cliente.id:  # ✅ dentro do for
                return {"erro": "Cliente com este ID já Registrado."}

    with open(file_clientes, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([cliente.id, cliente.nome, cliente.sobrenome, cliente.data_nascimento, cliente.cpf])

    return {"mensagem": "Cliente registrado com sucesso."}  # ✅ fora do with


@router.put("/update_clientes/{cliente_id}")
def atualizar_cliente(cliente_id: int, cliente: Cliente):
    clientes = []
    encontrado = False

    with open(file_clientes, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            if not row or len(row) < 2:
                continue

            if int(row[0]) == cliente_id:
                clientes.append([cliente.id, cliente.nome, cliente.sobrenome, cliente.data_nascimento, cliente.cpf])
                encontrado = True
            else:
                clientes.append(row)

    if not encontrado:
        return {"erro": "Cliente não encontrado."}

    with open(file_clientes, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "NOME", "SOBRENOME", "DATA_NASCIMENTO", "CPF"])
        writer.writerows(clientes)

    return {"mensagem": "Cliente atualizado com sucesso"}


@router.delete("/delete_clientes/{cliente_id}")
def deletar_cliente(cliente_id: int):
    clientes = []
    encontrado = False

    with open(file_clientes, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            if not row or len(row) < 2:
                continue

            if int(row[0]) == cliente_id:
                encontrado = True
            else:
                clientes.append(row)

    if not encontrado:
        return {"erro": "Cliente não encontrado."}

    with open(file_clientes, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "NOME", "SOBRENOME", "DATA_NASCIMENTO", "CPF"])
        writer.writerows(clientes)

    return {"mensagem": "Cliente deletado com sucesso."}