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

@app.get("/membro/{registrodoaluno}", response_model=MembroSchema, tags=["Membro"])
def get_membro_by_id_route(registrodoaluno: int, db: Session = Depends(get_db)):
    db_membro = get_membro_by_id(db, registrodoaluno)
    if not db_membro:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return db_membro
    
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

# Rotas para CelulaDeProjetos
@app.post("/projetos/", response_model=CelulaDeProjetosSchema, tags=["Célula de Projetos"])
def create_projeto_route(projeto: CelulaDeProjetosPublic, db: Session = Depends(get_db)):
    return create_projeto(db, projeto)

@app.get("/projetos/", response_model=List[CelulaDeProjetosSchema], tags=["Célula de Projetos"])
def get_all_projetos_route(db: Session = Depends(get_db)):
    return get_all_projetos(db)

@app.get("/projetos/{idprojeto}", response_model=CelulaDeProjetosSchema, tags=["Célula de Projetos"])
def get_projeto_route(idprojeto: int, db: Session = Depends(get_db)):
    db_projeto = get_projeto(db, idprojeto)
    if db_projeto is None:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return db_projeto

@app.put("/projetos/{idprojeto}", response_model=CelulaDeProjetosSchema, tags=["Célula de Projetos"])
def update_projeto_route(idprojeto: int, projeto: CelulaDeProjetosPublic, db: Session = Depends(get_db)):
    updated_projeto = update_projeto(db, idprojeto, projeto)
    if not updated_projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return updated_projeto

@app.delete("/projetos/{idprojeto}", response_model=dict, tags=["Célula de Projetos"])
def delete_projeto_route(idprojeto: int, db: Session = Depends(get_db)):
    deleted_response = delete_projeto(db, idprojeto)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return deleted_response

@app.post("/materiaprima/", response_model=MateriaPrimaSchema, tags=["Materia Prima"])
def create_materia_prima_route(materia_prima: MateriaPrimaPublic, db: Session = Depends(get_db)):
    return create_materia_prima(db, materia_prima)

@app.get("/materiaprima/", response_model=List[MateriaPrimaSchema], tags=["Materia Prima"])
def get_all_materia_prima_route(db: Session = Depends(get_db)):
    return get_all_materia_prima(db)

@app.get("/materiaprima/{idmateriaprima}", response_model=MateriaPrimaSchema, tags=["Materia Prima"])
def get_materia_prima_route(idmateriaprima: int, db: Session = Depends(get_db)):
    materia_prima = get_materia_prima(db, idmateriaprima)
    if not materia_prima:
        raise HTTPException(status_code=404, detail="Materia Prima não encontrada")
    return materia_prima

@app.put("/materiaprima/{idmateriaprima}", response_model=MateriaPrimaSchema, tags=["Materia Prima"])
def update_materia_prima_route(idmateriaprima: int, materia_prima: MateriaPrimaPublic, db: Session = Depends(get_db)):
    updated_materia_prima = update_materia_prima(db, idmateriaprima, materia_prima)
    if not updated_materia_prima:
        raise HTTPException(status_code=404, detail="Materia Prima não encontrada")
    return updated_materia_prima

@app.delete("/materiaprima/{idmateriaprima}", response_model=dict, tags=["Materia Prima"])
def delete_materia_prima_route(idmateriaprima: int, db: Session = Depends(get_db)):
    deleted_response = delete_materia_prima(db, idmateriaprima)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="Materia Prima não encontrada")
    return deleted_response

@app.post("/produto/", response_model=ProdutoSchema, tags=["Produto"])
def create_produto_route(produto: ProdutoPublic, db: Session = Depends(get_db)):
    return create_produto(db, produto)

@app.get("/produto/", response_model=List[ProdutoSchema], tags=["Produto"])
def get_all_produtos_route(db: Session = Depends(get_db)):
    return get_all_produtos(db)

@app.get("/produto/{idproduto}", response_model=ProdutoSchema, tags=["Produto"])
def get_produto_route(idproduto: int, db: Session = Depends(get_db)):
    produto = get_produto(db, idproduto)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.put("/produto/{idproduto}", response_model=ProdutoSchema, tags=["Produto"])
def update_produto_route(idproduto: int, produto: ProdutoPublic, db: Session = Depends(get_db)):
    updated_produto = update_produto(db, idproduto, produto)
    if not updated_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return updated_produto

@app.delete("/produto/{idproduto}", response_model=dict, tags=["Produto"])
def delete_produto_route(idproduto: int, db: Session = Depends(get_db)):
    deleted_response = delete_produto(db, idproduto)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return deleted_response

@app.post("/edital/", response_model=EditalSchema, tags=["Edital"])
def create_edital_route(edital: EditalPublic, db: Session = Depends(get_db)):
    return create_edital(db, edital)

@app.get("/edital/", response_model=List[EditalSchema], tags=["Edital"])
def get_all_editais_route(db: Session = Depends(get_db)):
    return get_all_editais(db)

@app.get("/edital/{idedital}", response_model=EditalSchema, tags=["Edital"])
def get_edital_route(idedital: int, db: Session = Depends(get_db)):
    edital = get_edital(db, idedital)
    if not edital:
        raise HTTPException(status_code=404, detail="Edital não encontrado")
    return edital

@app.put("/edital/{idedital}", response_model=EditalSchema, tags=["Edital"])
def update_edital_route(idedital: int, edital: EditalPublic, db: Session = Depends(get_db)):
    updated_edital = update_edital(db, idedital, edital)
    if not updated_edital:
        raise HTTPException(status_code=404, detail="Edital não encontrado")
    return updated_edital

@app.delete("/edital/{idedital}", response_model=dict, tags=["Edital"])
def delete_edital_route(idedital: int, db: Session = Depends(get_db)):
    deleted_response = delete_edital(db, idedital)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="Edital não encontrado")
    return deleted_response

@app.post("/localoficina/", response_model=LocalOficinaSchema, tags=["Local Oficina"])
def create_local_oficina_route(local_oficina: LocalOficinaPublic, db: Session = Depends(get_db)):
    return create_local_oficina(db, local_oficina)

@app.get("/localoficina/", response_model=List[LocalOficinaSchema], tags=["Local Oficina"])
def get_all_locais_oficina_route(db: Session = Depends(get_db)):
    return get_all_locais_oficina(db)

@app.get("/localoficina/{idlocal}", response_model=LocalOficinaSchema, tags=["Local Oficina"])
def get_local_oficina_route(idlocal: int, db: Session = Depends(get_db)):
    local_oficina = get_local_oficina(db, idlocal)
    if not local_oficina:
        raise HTTPException(status_code=404, detail="Local de Oficina não encontrado")
    return local_oficina

@app.put("/localoficina/{idlocal}", response_model=LocalOficinaSchema, tags=["Local Oficina"])
def update_local_oficina_route(idlocal: int, local_oficina: LocalOficinaPublic, db: Session = Depends(get_db)):
    updated_local_oficina = update_local_oficina(db, idlocal, local_oficina)
    if not updated_local_oficina:
        raise HTTPException(status_code=404, detail="Local de Oficina não encontrado")
    return updated_local_oficina

@app.delete("/localoficina/{idlocal}", response_model=dict, tags=["Local Oficina"])
def delete_local_oficina_route(idlocal: int, db: Session = Depends(get_db)):
    deleted_response = delete_local_oficina(db, idlocal)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="Local de Oficina não encontrado")
    return deleted_response

@app.post("/oficina/", response_model=OficinaSchema, tags=["Oficina"])
def create_oficina_route(oficina: OficinaPublic, db: Session = Depends(get_db)):
    return create_oficina(db, oficina)

@app.get("/oficina/", response_model=List[OficinaSchema], tags=["Oficina"])
def get_all_oficinas_route(db: Session = Depends(get_db)):
    return get_all_oficinas(db)

@app.get("/oficina/{idoficina}", response_model=OficinaSchema, tags=["Oficina"])
def get_oficina_route(idoficina: int, db: Session = Depends(get_db)):
    oficina = get_oficina(db, idoficina)
    if not oficina:
        raise HTTPException(status_code=404, detail="Oficina não encontrada")
    return oficina

@app.put("/oficina/{idoficina}", response_model=OficinaSchema, tags=["Oficina"])
def update_oficina_route(idoficina: int, oficina: OficinaPublic, db: Session = Depends(get_db)):
    updated_oficina = update_oficina(db, idoficina, oficina)
    if not updated_oficina:
        raise HTTPException(status_code=404, detail="Oficina não encontrada")
    return updated_oficina

@app.delete("/oficina/{idoficina}", response_model=dict, tags=["Oficina"])
def delete_oficina_route(idoficina: int, db: Session = Depends(get_db)):
    deleted_response = delete_oficina(db, idoficina)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="Oficina não encontrada")
    return deleted_response

@app.post("/pessoaauxiliada/", response_model=PessoaAuxiliadaSchema, tags=["Pessoa Auxiliada"])
def create_pessoa_auxiliada_route(pessoa: PessoaAuxiliadaPublic, db: Session = Depends(get_db)):
    return create_pessoa_auxiliada(db, pessoa)

@app.get("/pessoaauxiliada/", response_model=List[PessoaAuxiliadaSchema], tags=["Pessoa Auxiliada"])
def get_all_pessoas_auxiliadas_route(db: Session = Depends(get_db)):
    return get_all_pessoas_auxiliadas(db)

@app.get("/pessoaauxiliada/{idpessoa}", response_model=PessoaAuxiliadaSchema, tags=["Pessoa Auxiliada"])
def get_pessoa_auxiliada_route(idpessoa: int, db: Session = Depends(get_db)):
    pessoa = get_pessoa_auxiliada(db, idpessoa)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa auxiliada não encontrada")
    return pessoa

@app.put("/pessoaauxiliada/{idpessoa}", response_model=PessoaAuxiliadaSchema, tags=["Pessoa Auxiliada"])
def update_pessoa_auxiliada_route(idpessoa: int, pessoa: PessoaAuxiliadaPublic, db: Session = Depends(get_db)):
    updated_pessoa = update_pessoa_auxiliada(db, idpessoa, pessoa)
    if not updated_pessoa:
        raise HTTPException(status_code=404, detail="Pessoa auxiliada não encontrada")
    return updated_pessoa

@app.delete("/pessoaauxiliada/{idpessoa}", response_model=dict, tags=["Pessoa Auxiliada"])
def delete_pessoa_auxiliada_route(idpessoa: int, db: Session = Depends(get_db)):
    deleted_response = delete_pessoa_auxiliada(db, idpessoa)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="Pessoa auxiliada não encontrada")
    return deleted_response

@app.post("/membroprojeto/", response_model=MembroProjetoSchema, tags=["Membro Projeto"])
def create_membro_projeto_route(membro_projeto: MembroProjetoPublic, db: Session = Depends(get_db)):
    return create_membro_projeto(db, membro_projeto)

@app.get("/membroprojeto/{idprojeto}", response_model=List[MembroProjetoSchema], tags=["Membro Projeto"])
def get_membros_projeto_route(idprojeto: int, db: Session = Depends(get_db)):
    return get_membros_projeto(db, idprojeto)

@app.delete("/membroprojeto/{registrodoaluno}/{idprojeto}", response_model=dict, tags=["Membro Projeto"])
def delete_membro_projeto_route(registrodoaluno: int, idprojeto: int, db: Session = Depends(get_db)):
    deleted_response = delete_membro_projeto(db, registrodoaluno, idprojeto)
    if not deleted_response:
        raise HTTPException(status_code=404, detail="Membro não encontrado no projeto")
    return deleted_response