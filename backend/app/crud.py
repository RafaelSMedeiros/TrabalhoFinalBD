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