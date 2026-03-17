# 🛒 PROJETO API FASTAPI SUPERMERCADO

## 📌 Descrição

- Nesta atividade, o grupo desenvolveu uma **API RESTful** utilizando o **FastAPI**, que simula um sistema simples de gestão de um supermercado.

Essa API faz com seja possível alterar dados armazenados em **arquivos CSV**, utilizando os **métodos HTTP**:

- **GET:** Para **ler** ou buscar dados (ex: ver lista de produtos).
- **POST:** Para **criar** novos dados (ex: cadastrar um usuário).
- **PUT/PATCH:** Para **atualizar** dados (ex: mudar sua senha).
- **DELETE:** Para **remover** dados (ex: apaga um dado). 

---

## ⚙️ Tecnologias Utilizadas

- Python 
- FastAPI  
- CSV

---

## 📁 Estrutura de Dados (CSV)

Essa API gerencia os arquivos:


### 👤 Clientes.csv

| Campo | Tipo | Descrição |
|------|------|-----------|
| ID | int | Identificador único |
| Nome | str | Nome do cliente |
| Sobrenome | int | Sobrenome do cliente |
| Data de nascimento | int-int-int | Data de nascimento |
| CPF | str | CPF único | 


### 📦 Produtos.csv

| Método | Endpoint | Descrição |
|------|------|-----------|
| GET | `/produtos` | Lista  os produtos |
| POST | `/produtos` | Adiciona  novo produto |
| PUT | `/produtos` | Atualiza um produto |
| DELETE | `/produtos/{id}` | Remove um produto |


### 🧾 OrdemDeVendas.csv

| Método | Endpoint | Descrição |
|------|------|-----------|
| GET | `/ordens` | Lista as ordens de venda |
| POST | `/ordens` | Cria nova ordem de venda |
| PUT | `/ordens` | Atualiza uma ordem de venda |
| DELETE | `/ordens/{id}` | Remove uma ordem de venda | 


# 🔗 Endpoints da API


### 👤 Clientes

 - GET / clientes - Lista todos clientes 
 - POST / clientes - Adiciona novo cliente 
 - PUT / clientes - Atualiza um cliente que já existe 
 - DELETE / clientes - Remove um cliente 

---

### 📦 Produtos

 - GET / produtos - Lista todos produtos 
 - POST / produtos - Adiciona novo produto  
 - PUT / produtos - Atualiza um produto que já existe 
 - DELETE / produtos - Remove um produto 

---

### 🧾 Ordens de Venda
- GET / ordens - Lista todas as ordens das vendas 
- POST / ordens - Cria umas nova ordem para as vendas 
 - PUT / ordens - Atualiza uma ordem que já existe 
- DELETE / ordens - Remove uma ordem 

---

# 📏 Regras de Negócio

- O **ID de cada entidade é único**.
- Os **IDs são gerados automaticamente** pela API.
- Os dados são persistidos em **arquivos CSV**.


# ▶️ Como Executar o Projeto

### Clone o repositório

```bash
git clone https://github.com/Melhores-da-Sala/api-supermercado

2️⃣ Entrar na pasta do projeto
cd api-supermercado

3️⃣ Instalar as dependências
pip install fastapi 
pip install "fastapi[standard]"

4️⃣ Executar a API
fastapi dev app.py

5️⃣ Acessar a documentação automática

O FastAPI gera documentação automaticamente.

Swagger UI:

http://127.0.0.1:8000/docs

Redoc:

http://127.0.0.1:8000/redoc
```
---
# Explicação da API
- ## routes
  - ## cliente.py
     - ## GET
       - def listar_produtos():
         
     - ## POST
       - async def criar_produtos(produto: Produto):
         
     - ## DELETE
       - async def atualizar_dados(produto_id: int, produto: Produto):
         
     - ## PUT
       - def del_produto(produto_id: int):
       
  - ## produtos.py
     - ## GET
       -
       
     - ## POST
       -
       
     - ## DELETE
       -
       
     - ## PUT
       -
       
    
  - ## orden_de_venda.py
     - ## GET
       -
       
     - ## POST
       -
       
     - ## DELETE
       -
       
     - ## PUT
       -
       
