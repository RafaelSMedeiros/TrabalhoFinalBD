from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .crud import *
from .schemas import *
from typing import List

# Inicializando o app FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite requisições apenas de localhost:3000 (React)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Função para obter a sessão do banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criando o banco de dados se não existir
models.Base.metadata.create_all(bind=database.engine)

# Rotas do BackOffice
@app.post("/backoffice/", response_model=BackOfficeSchema, tags=["BackOffice"])
def create_backoffice_route(backoffice: BackOfficePublic, db: Session = Depends(get_db)):
    return create_backoffice(db, backoffice)

@app.get("/backoffice/", response_model=List[BackOfficeSchema], tags=["BackOffice"])
def get_all_backoffice_route(db: Session = Depends(get_db)):
    return get_all_backoffice(db)

@app.put("/backoffice/{idbackoffice}", response_model=BackOfficeSchema, tags=["BackOffice"])
def update_backoffice_route(idbackoffice: int, backoffice: BackOfficePublic, db: Session = Depends(get_db)):
    updated_backoffice = update_backoffice(db, idbackoffice, backoffice)
    if not updated_backoffice:
        raise HTTPException(status_code=404, detail="BackOffice não encontrado")
    return updated_backoffice

@app.delete("/backoffice/{idbackoffice}", response_model=dict, tags=["BackOffice"])
def delete_backoffice_route(idbackoffice: int, db: Session = Depends(get_db)):
    deleted_response = delete_backoffice(db, idbackoffice)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="BackOffice não encontrado")
    return deleted_response

# Rotas do Membro
@app.post("/membro/", response_model=MembroSchema, tags=["Membro"])
def create_membro_route(membro: MembroPublic, db: Session = Depends(get_db)):
    return create_membro(db, membro)

@app.get("/membro/", response_model=List[MembroSchema], tags=["Membro"])
def get_all_membros_route(db: Session = Depends(get_db)):
    return get_all_membros(db)

@app.put("/membro/{registrodoaluno}", response_model=MembroSchema, tags=["Membro"])
def update_membro_route(registrodoaluno: int, membro: MembroPublic, db: Session = Depends(get_db)):
    updated_membro = update_membro(db, registrodoaluno, membro)
    if not updated_membro:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return updated_membro

@app.delete("/membro/{registrodoaluno}", response_model=dict, tags=["Membro"])
def delete_membro_route(registrodoaluno: int, db: Session = Depends(get_db)):
    deleted_response = delete_membro(db, registrodoaluno)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return deleted_response

# Rotas da Planilha
@app.post("/planilhas/", response_model=PlanilhasSchema, tags=["Planilhas"])
def create_planilha_route(planilha: PlanilhasPublic, db: Session = Depends(get_db)):
    return create_planilha(db, planilha)

@app.get("/planilhas/", response_model=List[PlanilhasSchema], tags=["Planilhas"])
def get_all_planilhas_route(db: Session = Depends(get_db)):
    return get_all_planilhas(db)

@app.put("/planilhas/{idplanilha}", response_model=PlanilhasSchema, tags=["Planilhas"])
def update_planilha_route(idplanilha: int, planilha: PlanilhasPublic, db: Session = Depends(get_db)):
    updated_planilha = update_planilha(db, idplanilha, planilha)
    if not updated_planilha:
        raise HTTPException(status_code=404, detail="Planilha não encontrada")
    return updated_planilha

@app.delete("/planilhas/{idplanilha}", response_model=dict, tags=["Planilhas"])
def delete_planilha_route(idplanilha: int, db: Session = Depends(get_db)):
    deleted_response = delete_planilha(db, idplanilha)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="Planilha não encontrada")
    return deleted_response

# Rotas de Posts
@app.post("/posts/", response_model=PostsSchema, tags=["Posts"])
def create_post_route(post: PostsPublic, db: Session = Depends(get_db)):
    return create_post(db, post)

@app.get("/posts/", response_model=List[PostsSchema], tags=["Posts"])
def get_all_posts_route(db: Session = Depends(get_db)):
    return get_all_posts(db)

@app.get("/posts/{idpost}", response_model=PostsSchema, tags=["Posts"])
def get_post_route(idpost: int, db: Session = Depends(get_db)):
    db_post = get_post(db, idpost)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    return db_post

@app.put("/posts/{idpost}", response_model=PostsSchema, tags=["Posts"])
def update_post_route(idpost: int, post: PostsPublic, db: Session = Depends(get_db)):
    updated_post = update_post(db, idpost, post)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    return updated_post

@app.delete("/posts/{idpost}", response_model=dict, tags=["Posts"])
def delete_post_route(idpost: int, db: Session = Depends(get_db)):
    deleted_response = delete_post(db, idpost)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    return deleted_response