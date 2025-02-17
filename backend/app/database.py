# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:novasenha@localhost:5434/projetodb"  # Substitua a senha e o banco conforme necessário

# Criando a engine
engine = create_engine(DATABASE_URL, echo=True)

# Sessão local para interações com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de dados para os modelos
Base = declarative_base()
