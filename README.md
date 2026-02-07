# Library Manager (SQLite3 Puro)

> Sistema de gerenciamento de biblioteca pessoal desenvolvido em Python. O foco deste projeto foi explorar a persistência de dados utilizando **SQL Puro (Raw SQL)** e a biblioteca nativa `sqlite3`, sem o uso de ORMs, garantindo controle total sobre as queries e performance.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite3-003B57?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Concluído-green)

## Objetivos do Desafio

Este projeto faz parte de um desafio de estudos focado em fundamentos. Os principais conceitos aplicados foram:

* **Persistência de Dados:** Criação e manutenção de arquivos `.db`.
* **CRUD Completo:** Inserção, Leitura, Atualização e Deleção de registros.
* **Segurança:** Uso de *Parameterized Queries* (`?`) para prevenir SQL Injection.
* **Context Managers:** Uso de `with sqlite3.connect()` para garantir o fechamento seguro das conexões.

## Estrutura do Projeto

```text
LibrarySQLite3/
├── 📂 data/             # Armazenamento do Banco de Dados (dataBooks.db)
├── 📂 models/           # Definição de Classes/Entidades
│   └── book.py          # Classe Book
├── 📂 services/         # Lógica de Negócio e Acesso ao Banco
│   └── system.py        # Queries SQL e Regras (System Class)
├── main.py              # Interface de Linha de Comando (CLI)
└── README.md            # Documentação

```

## 🛠️ Funcionalidades

O sistema oferece um menu interativo no terminal com as seguintes opções:

1. **Registrar Livro:** Salva título, autor e ano de lançamento. O status inicial é "Não Lido".
2. **Atualizar Status:** Permite marcar um livro como "Lido" (Update).
3. **Modo de Busca e Leitura:**
* Buscar livro por título (busca parcial com `LIKE`).
* Listar todos os livros.
* Filtrar apenas livros Lidos.
* Filtrar apenas livros Não Lidos.


4. **Modo de Deleção:**
* Deletar um livro específico (por ID).
* **Nuke Mode:** Deletar todos os livros (Requer senha de segurança: `DELETEALLDATABASE`).



## Como Executar

### Pré-requisitos

* Python 3 instalado.

### Passo a Passo

1. Clone o repositório ou baixe os arquivos.
2. Navegue até a pasta raiz do projeto.
3. Execute o arquivo principal:

```bash
python main.py

```

O banco de dados `data/dataBooks.db` será criado automaticamente na primeira execução.

## Destaques de Implementação

### Prevenção de SQL Injection

Ao invés de concatenar strings (o que seria perigoso), o projeto utiliza a substituição segura de parâmetros oferecida pelo driver do SQLite:

```python
# Correto (Seguro)
sql_query = "INSERT INTO books (title, writer, year, state_Read) VALUES (?, ?, ?, ?)"
cur.execute(sql_query, (book.title, book.writer, book.year, book.state_Read))

```

### Validação de Segurança

Para operações destrutivas (apagar todo o banco), foi implementada uma camada lógica de confirmação dupla:

```python
if user_type_securety == "DELETEALLDATABASE":
    cur.execute("DELETE FROM books")
    con.commit()

```

---

Desenvolvido por **Nicolas Cleik de Andrade** como parte do desafio de estudos "Hard Mode", como exemplo de **Boas Práticas em Python**.

```