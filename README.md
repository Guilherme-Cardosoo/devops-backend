# DevOps Backend

Backend da aplicação desenvolvido utilizando FastAPI e PostgreSQL.

## Objetivo

Este projeto disponibiliza uma API REST responsável pelo gerenciamento dos produtos da aplicação, realizando operações de cadastro, consulta, edição e remoção de registros armazenados em um banco PostgreSQL.

## Tecnologias Utilizadas

- Python 3
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- Docker

## Executando Localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure a variável de ambiente:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/devops
```

Inicie a aplicação:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

```
http://localhost:8000
```

## Documentação da API

A documentação automática do FastAPI pode ser acessada em:

```
http://localhost:8000/docs
```

## Docker

Construir a imagem:

```bash
docker build -t devops-backend .
```

Executar o container:

```bash
docker run -p 8000:8000 devops-backend
```

## Docker Hub

Imagem publicada:

```
guiihermecardoso/devops-backend:latest
```

## Banco de Dados

O projeto utiliza PostgreSQL como banco de dados e SQLAlchemy como ORM para comunicação com a base de dados.

## Autor

Guilherme Cardoso

Projeto desenvolvido como trabalho final da disciplina de DevOps.