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

class CelulaDeProjetosSchema(BaseModel):
    idprojeto: int
    descricaoprojeto: str = None
    odsprojeto: str = None
    nomeprojeto: str

    class Config:
        orm_mode = True

class CelulaDeProjetosPublic(BaseModel):
    descricaoprojeto: str = None
    odsprojeto: str = None
    nomeprojeto: str

# Materia Prima
class MateriaPrimaSchema(BaseModel):
    idmateriaprima: int
    tipomateriaprima: str
    quantidademateriaprima: int
    precomateriaprima: float
    marcamateriaprima: str

    class Config:
        orm_mode = True

class MateriaPrimaPublic(BaseModel):
    tipomateriaprima: str
    quantidademateriaprima: int
    precomateriaprima: float
    marcamateriaprima: str

# Produto
class ProdutoSchema(BaseModel):
    idproduto: int
    descricaoproduto: str
    nomeproduto: str
    publicoalvo: str
    idprojeto: int

    class Config:
        orm_mode = True

class ProdutoPublic(BaseModel):
    descricaoproduto: str
    nomeproduto: str
    publicoalvo: str
    idprojeto: int

# Edital
class EditalSchema(BaseModel):
    idedital: int
    empresa: str
    datafinal: date
    premio: float
    requisitos: str

    class Config:
        orm_mode = True

class EditalPublic(BaseModel):
    empresa: str
    datafinal: date
    premio: float
    requisitos: str

class LocalOficinaSchema(BaseModel):
    idlocal: int
    tipolocal: str = None
    enderecolocal: str = None
    descricaolocal: str = None
    nomelocal: str

    class Config:
        orm_mode = True

class LocalOficinaPublic(BaseModel):
    tipolocal: str = None
    enderecolocal: str = None
    descricaolocal: str = None
    nomelocal: str

class OficinaSchema(BaseModel):
    idoficina: int
    tipooficina: str = None
    descricaooficina: str = None
    idprojeto: int = None
    dataoficina: date = None
    idlocal: int = None

    class Config:
        orm_mode = True

class OficinaPublic(BaseModel):
    tipooficina: str = None
    descricaooficina: str = None
    idprojeto: int = None
    dataoficina: date = None
    idlocal: int = None

class PessoaAuxiliadaSchema(BaseModel):
    idpessoa: int
    racapessoa: Optional[str] = None
    cpfpessoa: str
    nomepessoa: str
    enderecopessoa: Optional[str] = None
    rendapessoa: Optional[float] = None
    sexopessoa: Optional[str] = None
    tamanhodafamilia: Optional[int] = None
    chavepix: Optional[str] = None

    class Config:
        orm_mode = True

class PessoaAuxiliadaPublic(BaseModel):
    racapessoa: Optional[str] = None
    cpfpessoa: str
    nomepessoa: str
    enderecopessoa: Optional[str] = None
    rendapessoa: Optional[float] = None
    sexopessoa: Optional[str] = None
    tamanhodafamilia: Optional[int] = None
    chavepix: Optional[str] = None
