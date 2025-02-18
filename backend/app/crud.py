from sqlalchemy.orm import Session
from .models import *
from .schemas import *
from typing import List

def create_backoffice(db: Session, backoffice: BackOfficePublic):
    db_backoffice = BackOffice(descricaobackoffice=backoffice.descricaobackoffice)
    db.add(db_backoffice)
    db.commit()
    db.refresh(db_backoffice)
    return db_backoffice

def get_all_backoffice(db: Session) -> List[BackOffice]:
    return db.query(BackOffice).all()

def update_backoffice(db: Session, idbackoffice: int, backoffice: BackOfficePublic):
    db_backoffice = db.query(BackOffice).filter(BackOffice.idbackoffice == idbackoffice).first()
    if not db_backoffice:
        return None
    db_backoffice.descricaobackoffice = backoffice.descricaobackoffice
    db.commit()
    db.refresh(db_backoffice)
    return db_backoffice

def delete_backoffice(db: Session, idbackoffice: int):
    db_backoffice = db.query(BackOffice).filter(BackOffice.idbackoffice == idbackoffice).first()
    if not db_backoffice:
        return None
    db.delete(db_backoffice)
    db.commit()
    return {"detail": "BackOffice deletado com sucesso"}

def create_membro(db: Session, membro: MembroSchema):
    db_membro = Membro(
        registrodoaluno=membro.registrodoaluno,  # Certifique-se de que está sendo enviado
        nomealuno=membro.nomealuno,
        cursoaluno=membro.cursoaluno,
        emailaluno=membro.emailaluno,
        telefonealuno=membro.telefonealuno,
        idbackoffice=membro.idbackoffice
    )
    db.add(db_membro)
    db.commit()
    db.refresh(db_membro)
    return db_membro

def get_all_membros(db: Session) -> List[Membro]:
    return db.query(Membro).all()

def update_membro(db: Session, registrodoaluno: int, membro: MembroPublic):
    db_membro = db.query(Membro).filter(Membro.registrodoaluno == registrodoaluno).first()
    if not db_membro:
        return None
    for key, value in membro.dict(exclude_unset=True).items():
        setattr(db_membro, key, value)
    db.commit()
    db.refresh(db_membro)
    return db_membro

def delete_membro(db: Session, registrodoaluno: int):
    db_membro = db.query(Membro).filter(Membro.registrodoaluno == registrodoaluno).first()
    if not db_membro:
        return None
    db.delete(db_membro)
    db.commit()
    return {"detail": "Membro deletado com sucesso"}

def create_planilha(db: Session, planilha: PlanilhasPublic):
    db_planilha = Planilhas(
        topicoplanilha=planilha.topicoplanilha,
        descricaoplanilha=planilha.descricaoplanilha,
        conteudoplanilha=planilha.conteudoplanilha
    )
    db.add(db_planilha)
    db.commit()
    db.refresh(db_planilha)
    return db_planilha

def get_all_planilhas(db: Session):
    return db.query(Planilhas).all()

def update_planilha(db: Session, idplanilha: int, planilha: PlanilhasPublic):
    db_planilha = db.query(Planilhas).filter(Planilhas.idplanilha == idplanilha).first()
    if not db_planilha:
        return None
    db_planilha.topicoplanilha = planilha.topicoplanilha
    db_planilha.descricaoplanilha = planilha.descricaoplanilha
    db_planilha.conteudoplanilha = planilha.conteudoplanilha
    db.commit()
    db.refresh(db_planilha)
    return db_planilha

def delete_planilha(db: Session, idplanilha: int):
    db_planilha = db.query(Planilhas).filter(Planilhas.idplanilha == idplanilha).first()
    if not db_planilha:
        return None
    db.delete(db_planilha)
    db.commit()
    return {"detail": "Planilha deletada com sucesso"}

def create_post(db: Session, post: PostsPublic):
    db_post = Posts(
        assuntopost=post.assuntopost,
        titulopost=post.titulopost,
        descricaopost=post.descricaopost,
        anexos=post.anexos,
        datapublicacao=post.datapublicacao
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Obter todos os posts
def get_all_posts(db: Session):
    return db.query(Posts).all()

# Obter um post específico
def get_post(db: Session, idpost: int):
    return db.query(Posts).filter(Posts.idpost == idpost).first()

# Atualizar um post
def update_post(db: Session, idpost: int, post: PostsPublic):
    db_post = db.query(Posts).filter(Posts.idpost == idpost).first()
    if db_post:
        db_post.assuntopost = post.assuntopost
        db_post.titulopost = post.titulopost
        db_post.descricaopost = post.descricaopost
        db_post.anexos = post.anexos
        db_post.datapublicacao = post.datapublicacao
        db.commit()
        db.refresh(db_post)
        return db_post
    return None

# Deletar um post
def delete_post(db: Session, idpost: int):
    db_post = db.query(Posts).filter(Posts.idpost == idpost).first()
    if db_post:
        db.delete(db_post)
        db.commit()
        return {"message": "Post deletado com sucesso"}
    return None

def create_projeto(db: Session, projeto: CelulaDeProjetosPublic):
    db_projeto = CelulaDeProjetos(
        descricaoprojeto=projeto.descricaoprojeto,
        odsprojeto=projeto.odsprojeto,
        nomeprojeto=projeto.nomeprojeto
    )
    db.add(db_projeto)
    db.commit()
    db.refresh(db_projeto)
    return db_projeto

def get_all_projetos(db: Session):
    return db.query(CelulaDeProjetos).all()

def get_projeto(db: Session, idprojeto: int):
    return db.query(CelulaDeProjetos).filter(CelulaDeProjetos.idprojeto == idprojeto).first()

def update_projeto(db: Session, idprojeto: int, projeto: CelulaDeProjetosPublic):
    db_projeto = db.query(CelulaDeProjetos).filter(CelulaDeProjetos.idprojeto == idprojeto).first()
    if db_projeto:
        db_projeto.descricaoprojeto = projeto.descricaoprojeto
        db_projeto.odsprojeto = projeto.odsprojeto
        db_projeto.nomeprojeto = projeto.nomeprojeto
        db.commit()
        db.refresh(db_projeto)
        return db_projeto
    return None

def delete_projeto(db: Session, idprojeto: int):
    db_projeto = db.query(CelulaDeProjetos).filter(CelulaDeProjetos.idprojeto == idprojeto).first()
    if db_projeto:
        db.delete(db_projeto)
        db.commit()
        return {"message": "Projeto deletado com sucesso"}
    return None

def create_materia_prima(db: Session, materia_prima: MateriaPrimaPublic):
    db_materia_prima = MateriaPrima(**materia_prima.dict())
    db.add(db_materia_prima)
    db.commit()
    db.refresh(db_materia_prima)
    return db_materia_prima

def get_all_materia_prima(db: Session):
    return db.query(MateriaPrima).all()

def get_materia_prima(db: Session, idmateriaprima: int):
    return db.query(MateriaPrima).filter(MateriaPrima.idmateriaprima == idmateriaprima).first()

def update_materia_prima(db: Session, idmateriaprima: int, materia_prima: MateriaPrimaPublic):
    db_materia_prima = db.query(MateriaPrima).filter(MateriaPrima.idmateriaprima == idmateriaprima).first()
    if db_materia_prima:
        for key, value in materia_prima.dict().items():
            setattr(db_materia_prima, key, value)
        db.commit()
        db.refresh(db_materia_prima)
        return db_materia_prima
    return None

def delete_materia_prima(db: Session, idmateriaprima: int):
    db_materia_prima = db.query(MateriaPrima).filter(MateriaPrima.idmateriaprima == idmateriaprima).first()
    if db_materia_prima:
        db.delete(db_materia_prima)
        db.commit()
        return {"message": "Materia Prima deletada com sucesso"}
    return None

# CRUD Produto
def create_produto(db: Session, produto: ProdutoPublic):
    db_produto = Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def get_all_produtos(db: Session):
    return db.query(Produto).all()

def get_produto(db: Session, idproduto: int):
    return db.query(Produto).filter(Produto.idproduto == idproduto).first()

def update_produto(db: Session, idproduto: int, produto: ProdutoPublic):
    db_produto = db.query(Produto).filter(Produto.idproduto == idproduto).first()
    if db_produto:
        for key, value in produto.dict().items():
            setattr(db_produto, key, value)
        db.commit()
        db.refresh(db_produto)
        return db_produto
    return None

def delete_produto(db: Session, idproduto: int):
    db_produto = db.query(Produto).filter(Produto.idproduto == idproduto).first()
    if db_produto:
        db.delete(db_produto)
        db.commit()
        return {"message": "Produto deletado com sucesso"}
    return None

# CRUD Edital
def create_edital(db: Session, edital: EditalPublic):
    db_edital = Edital(**edital.dict())
    db.add(db_edital)
    db.commit()
    db.refresh(db_edital)
    return db_edital

def get_all_editais(db: Session):
    return db.query(Edital).all()

def get_edital(db: Session, idedital: int):
    return db.query(Edital).filter(Edital.idedital == idedital).first()

def update_edital(db: Session, idedital: int, edital: EditalPublic):
    db_edital = db.query(Edital).filter(Edital.idedital == idedital).first()
    if db_edital:
        for key, value in edital.dict().items():
            setattr(db_edital, key, value)
        db.commit()
        db.refresh(db_edital)
        return db_edital
    return None

def delete_edital(db: Session, idedital: int):
    db_edital = db.query(Edital).filter(Edital.idedital == idedital).first()
    if db_edital:
        db.delete(db_edital)
        db.commit()
        return {"message": "Edital deletado com sucesso"}
    return None


def create_local_oficina(db: Session, local_oficina: LocalOficinaPublic):
    db_local_oficina = LocalOficina(**local_oficina.dict())
    db.add(db_local_oficina)
    db.commit()
    db.refresh(db_local_oficina)
    return db_local_oficina

def get_all_locais_oficina(db: Session):
    return db.query(LocalOficina).all()

def get_local_oficina(db: Session, idlocal: int):
    return db.query(LocalOficina).filter(LocalOficina.idlocal == idlocal).first()

def update_local_oficina(db: Session, idlocal: int, local_oficina: LocalOficinaPublic):
    db_local_oficina = db.query(LocalOficina).filter(LocalOficina.idlocal == idlocal).first()
    if not db_local_oficina:
        return None
    for key, value in local_oficina.dict(exclude_unset=True).items():
        setattr(db_local_oficina, key, value)
    db.commit()
    db.refresh(db_local_oficina)
    return db_local_oficina

def delete_local_oficina(db: Session, idlocal: int):
    db_local_oficina = db.query(LocalOficina).filter(LocalOficina.idlocal == idlocal).first()
    if not db_local_oficina:
        return None
    db.delete(db_local_oficina)
    db.commit()
    return {"message": "Local de Oficina deletado com sucesso"}

def create_oficina(db: Session, oficina: OficinaPublic):
    db_oficina = Oficina(**oficina.dict())
    db.add(db_oficina)
    db.commit()
    db.refresh(db_oficina)
    return db_oficina

def get_all_oficinas(db: Session):
    return db.query(Oficina).all()

def get_oficina(db: Session, idoficina: int):
    return db.query(Oficina).filter(Oficina.idoficina == idoficina).first()

def update_oficina(db: Session, idoficina: int, oficina: OficinaPublic):
    db_oficina = db.query(Oficina).filter(Oficina.idoficina == idoficina).first()
    if not db_oficina:
        return None
    for key, value in oficina.dict(exclude_unset=True).items():
        setattr(db_oficina, key, value)
    db.commit()
    db.refresh(db_oficina)
    return db_oficina

def delete_oficina(db: Session, idoficina: int):
    db_oficina = db.query(Oficina).filter(Oficina.idoficina == idoficina).first()
    if not db_oficina:
        return None
    db.delete(db_oficina)
    db.commit()
    return {"message": "Oficina deletada com sucesso"}

def create_pessoa_auxiliada(db: Session, pessoa: PessoaAuxiliadaPublic):
    db_pessoa = PessoaAuxiliada(**pessoa.dict())
    db.add(db_pessoa)
    db.commit()
    db.refresh(db_pessoa)
    return db_pessoa

def get_all_pessoas_auxiliadas(db: Session):
    return db.query(PessoaAuxiliada).all()

def get_pessoa_auxiliada(db: Session, idpessoa: int):
    return db.query(PessoaAuxiliada).filter(PessoaAuxiliada.idpessoa == idpessoa).first()

def update_pessoa_auxiliada(db: Session, idpessoa: int, pessoa: PessoaAuxiliadaPublic):
    db_pessoa = db.query(PessoaAuxiliada).filter(PessoaAuxiliada.idpessoa == idpessoa).first()
    if not db_pessoa:
        return None
    for key, value in pessoa.dict(exclude_unset=True).items():
        setattr(db_pessoa, key, value)
    db.commit()
    db.refresh(db_pessoa)
    return db_pessoa

def delete_pessoa_auxiliada(db: Session, idpessoa: int):
    db_pessoa = db.query(PessoaAuxiliada).filter(PessoaAuxiliada.idpessoa == idpessoa).first()
    if not db_pessoa:
        return None
    db.delete(db_pessoa)
    db.commit()
    return {"message": "Pessoa auxiliada deletada com sucesso"}
