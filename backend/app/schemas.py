from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class BackOfficeSchema(BaseModel):
    idbackoffice: int
    descricaobackoffice: str
    class Config:
        orm_mode = True

class BackOfficePublic(BaseModel):
    descricaobackoffice: str

class MembroSchema(BaseModel):
    registrodoaluno: int
    nomealuno: str
    cursoaluno: str
    emailaluno: str
    telefonealuno: str
    idbackoffice: int

    class Config:
        orm_mode = True

class MembroPublic(BaseModel):
    registrodoaluno: int
    nomealuno: str
    cursoaluno: Optional[str] = None
    emailaluno: Optional[str] = None
    telefonealuno: Optional[str] = None
    idbackoffice: Optional[int] = None

class PlanilhasSchema(BaseModel):
    idplanilha: int
    topicoplanilha: str
    descricaoplanilha: Optional[str] = None
    conteudoplanilha: Optional[str] = None

    class Config:
        orm_mode = True

class PlanilhasPublic(BaseModel):
    topicoplanilha: str
    descricaoplanilha: Optional[str] = None
    conteudoplanilha: Optional[str] = None

class PostsSchema(BaseModel):
    idpost: int
    assuntopost: str
    titulopost: str = None
    descricaopost: str = None
    anexos: str = None
    datapublicacao: date

    class Config:
        orm_mode = True

class PostsPublic(BaseModel):
    assuntopost: str
    titulopost: str = None
    descricaopost: str = None
    anexos: str = None
    datapublicacao: date
