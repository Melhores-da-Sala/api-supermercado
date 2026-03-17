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

### 📄 `cliente.py`
Gerencia o cadastro de clientes com foco em integridade de dados.

* <kbd> <font color="green">**GET**</font> </kbd> **`listar_clientes()`**
  - **Lógica:** Abre o arquivo `Clientes.csv` em modo leitura (`r`), converte as linhas para dicionários e retorna a lista completa.

* <kbd> <font color="orange">**POST**</font> </kbd> **`criar_clientes()`**
  - **ID Único:** Inicia a variável `novo_id` em 1. O código percorre o CSV e, para cada registro encontrado, atualiza: `novo_id = id_da_linha + 1`. Isso garante que o novo ID seja sempre o próximo da sequência.
  - **CPF Único:** Antes de salvar, o sistema faz um loop no arquivo comparando o CPF enviado. Se houver duplicidade, o cadastro é interrompido com uma mensagem de erro.

* <kbd> <font color="blue">**PUT**</font> </kbd> **`atualizar_dados()`**
  - **Lógica:** Localiza o cliente pelo ID informado na URL. Se encontrado, substitui os valores daquela linha pelos novos dados e reescreve o arquivo CSV inteiro.

* <kbd> <font color="red">**DELETE**</font> </kbd> **`del_cliente()`**
  - **Lógica:** Lê o arquivo e gera uma nova lista de dados **ignorando** a linha que possui o ID selecionado. Em seguida, salva o arquivo apenas com os registros restantes.

---

### 📄 `produtos.py`
Responsável pelo controle de inventário e fornecedores.

* <kbd> <font color="green">**GET**</font> </kbd> **`listar_produtos()`**
  - **Lógica:** Consulta o `Produtos.csv` e retorna o estado atual do estoque (nome, fornecedor e quantidade).

* <kbd> <font color="orange">**POST**</font> </kbd> **`criar_produtos()`**
  - **ID Automático:** Segue a mesma lógica de varredura (Último ID + 1) para manter a organização dos itens.

* <kbd> <font color="blue">**PUT**</font> </kbd> **`atualizar_dados()`**
  - **Lógica:** Utilizado para editar informações do produto ou atualizar a quantidade em estoque após reposições.

* <kbd> <font color="red">**DELETE**</font> </kbd> **`del_produto()`**
  - **Lógica:** Remove o item do arquivo. Como os arquivos não possuem chaves estrangeiras físicas, a venda vinculada a este ID em outros arquivos permanecerá lá como um registro "órfão".

---

### 📄 `ordem_de_venda.py`
Registra a transação comercial entre Clientes e Produtos.

* <kbd> <font color="green">**GET**</font> </kbd> **`listar_vendas()`**
  - **Lógica:** Retorna o histórico de todas as operações de venda realizadas.

* <kbd> <font color="orange">**POST**</font> </kbd> **`criar_venda()`**
  - **Lógica:** Recebe o `cliente_id` e o `produto_id`. Gera um `id_ordem` automático e grava a nova transação no arquivo `OrdemDeVendas.csv`.

* <kbd> <font color="red">**DELETE**</font> </kbd> **`del_venda()`**
  - **Lógica:** Permite a exclusão de um registro de venda através do ID da ordem.

---
