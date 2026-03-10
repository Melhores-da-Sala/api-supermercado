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

@router.get("/clientes")
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
