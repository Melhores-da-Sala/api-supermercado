from app import *

#class Produto(BaseModel):
#    id: int
#    nome: str
#    fornecedor: str
#    quantidade: int
#################################### GET #####################################
@app.get("/produtos")
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
@app.post("/produtos")
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
@app.delete("/produtos/{id}")
def deletar_produtos():
    pass
##############################################################################
#################################### PUT #####################################
@app.put("/produtos")
async def atualizar_dados():
    pass
##############################################################################