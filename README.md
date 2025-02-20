# Trabalho Final - Banco de Dados

Sistema de banco de dados e interface CRUD para a Enactus UNIFESP - São José dos Campos.

## 📌 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/RafaelSMedeiros/TrabalhoFinalBD
```

## 📋 Pré-requisitos

Certifique-se de ter o **PostgreSQL** instalado e rodando.

Conecte-se ao banco de dados:
```bash
psql postgresql://postgres:SUA_SENHA@localhost:5434/SEU_BANCO
```

Execute o script SQL para configurar o banco de dados:
```sql
\i guiDatabase.sql
```

### 2. Configuração do Backend
Acesse a pasta do backend:
```bash
cd backend
```

Crie e inicialize um ambiente virtual Python:
```bash
python -m venv venv
```

Ative o ambiente virtual:
#### No Windows (PowerShell)
```powershell
.\venv\Scripts\Activate
```
#### No Linux/MacOS
```bash
source venv/bin/activate
```

Instale as dependências do backend:
```bash
pip install -r requirements.txt
```

## 🚀 Uso

### 1. Iniciar o Backend
Execute a API com o seguinte comando:
```bash
uvicorn app.main:app --reload --port 8000
```

### 2. Configuração do Frontend
Acesse a pasta do frontend:
```bash
cd frontend
```

Instale as dependências:
```bash
npm install
```

### 3. Iniciar o Frontend
Inicie com o seguinte comando:
```bash
npm start
```

## 🛠 Tecnologias Utilizadas
- **Backend:** FastAPI, PostgreSQL
- **Frontend:** React, Axios
- **Banco de Dados:** PostgreSQL

