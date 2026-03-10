# 🛒 PROJETO API FLASK SUPERMERCADO

## 📌 Descrição

Nesta atividade, o grupo desenvolveu uma **API RESTful** fazendo o uso do **FastAPI**, que representa um sistema simples de administração de um supermercado.

Essa API faz com seja possível alterar dados armazenados em **arquivos CSV**, utilizando os **métodos HTTP**:

- **GET:** Para **ler** ou buscar dados (ex: ver lista de produtos).
- **POST:** Para **criar** novos dados (ex: cadastrar um usuário).
- **PUT/PATCH:** Para **atualizar** dados (ex: mudar sua senha).
- **DELETE:** Para **remover** dados (ex: apagar uma foto).

---

# ⚙️ Tecnologias e linguagens utilizadas

- **Python**
- **FastAPI**
- **CSV** (para armazenamento de dados)

---

# 📁 Estrutura de Dados - Arquivos CSV

Essa API gerencia os arquivos:

# 👤 Clientes.csv

| Campo | Tipo | Descrição |
|------|------|-----------|
| ID | int | Identificador único |
| Nome | str | Nome do cliente |
| Sobrenome | int | Sobrenome do cliente |
| Data de nascimento | int-int-int | Data de nascimento |
| CPF | str | CPF único |

---

# 📦 Produtos.csv

| Campo | Tipo | Descrição |
|------|------|-----------|
| ID | int | Identificador único |
| Nome | str | Nome do produto |
| Fornecedor | str | Empresa fornecedora |
| Quantidade | int | Quantidade em estoque |

---

# 🧾 OrdemDeVendas.csv

| Campo | Tipo | Descrição |
|------|------|-----------|
| ID da Ordem | int | Identificador único da venda |
| Cliente | int | ID do cliente |
| Produto | int | ID do produto |

---

# 🔗 Endpoints da API

## 👤 Clientes

| Método | Endpoint | Descrição |
|------|------|-----------|
| GET | `/clientes` | Lista os clientes |
| POST | `/clientes` | Adiciona novo cliente |
| PUT | `/clientes` | Atualiza um cliente |
| DELETE | `/clientes/{id}` | Remove um cliente |

---

## 📦 Produtos

| Método | Endpoint | Descrição |
|------|------|-----------|
| GET | `/produtos` | Lista  os produtos |
| POST | `/produtos` | Adiciona  novo produto |
| PUT | `/produtos` | Atualiza um produto |
| DELETE | `/produtos/{id}` | Remove um produto |

---

## 🧾 Ordens de Venda

| Método | Endpoint | Descrição |
|------|------|-----------|
| GET | `/ordens` | Lista as ordens de venda |
| POST | `/ordens` | Cria nova ordem de venda |
| PUT | `/ordens` | Atualiza uma ordem de venda |
| DELETE | `/ordens/{id}` | Remove uma ordem de venda |

---

# 📏 Regras de Negócio

- O **ID de cada entidade é único**.
- Os **IDs são gerados automaticamente** pela API.
- Os dados são persistidos em **arquivos CSV**.

---

# ▶️ Como Executar o Projeto

### Clone o repositório

```bash
git clone https://github.com/Melhores-da-Sala/api-supermercado
