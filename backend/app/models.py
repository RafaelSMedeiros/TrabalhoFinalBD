from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BackOffice(Base):
    __tablename__ = 'backoffice'

    idbackoffice = Column(Integer, primary_key=True, autoincrement=True)
    descricaobackoffice = Column(String(200), nullable=False)
    membros = relationship("Membro", back_populates="backoffice")

class Membro(Base):
    __tablename__ = 'membro'

    registrodoaluno = Column(Integer, primary_key=True)
    nomealuno = Column(String(100), nullable=False)
    cursoaluno = Column(String(100))
    emailaluno = Column(String(100))
    telefonealuno = Column(String(20))
    idbackoffice = Column(Integer, ForeignKey('backoffice.idbackoffice'))
    backoffice = relationship("BackOffice", back_populates="membros")

class Planilhas(Base):
    __tablename__ = 'planilhas'

    idplanilha = Column(Integer, primary_key=True, autoincrement=True)
    topicoplanilha = Column(String(100), nullable=False)
    descricaoplanilha = Column(String(200))
    conteudoplanilha = Column(String(200))

class Posts(Base):
    __tablename__ = 'posts'

    idpost = Column(Integer, primary_key=True, autoincrement=True)
    assuntopost = Column(String(100), nullable=False)
    titulopost = Column(String(100))
    descricaopost = Column(String(200))
    anexos = Column(String(100))
    datapublicacao = Column(Date)

class CelulaDeProjetos(Base):
    __tablename__ = 'celuladeprojetos'

    idprojeto = Column(Integer, primary_key=True, autoincrement=True)
    descricaoprojeto = Column(String(200))
    odsprojeto = Column(String(100))
    nomeprojeto = Column(String(100), nullable=False)

class MateriaPrima(Base):
    __tablename__ = 'materiaprima'

    idmateriaprima = Column(Integer, primary_key=True, autoincrement=True)
    tipomateriaprima = Column(String(100))
    quantidademateriaprima = Column(Integer)
    precomateriaprima = Column(Float)
    marcamateriaprima = Column(String(100))

class Produto(Base):
    __tablename__ = 'produto'

    idproduto = Column(Integer, primary_key=True, autoincrement=True)
    descricaoproduto = Column(String(200))
    nomeproduto = Column(String(100))
    publicoalvo = Column(String(100))
    idprojeto = Column(Integer, ForeignKey('celuladeprojetos.idprojeto'))

class Edital(Base):
    __tablename__ = 'edital'

    idedital = Column(Integer, primary_key=True, autoincrement=True)
    empresa = Column(String(100))
    datafinal = Column(Date)
    premio = Column(Float)
    requisitos = Column(String(200))

class LocalOficina(Base):
    __tablename__ = 'localoficina'

    idlocal = Column(Integer, primary_key=True, autoincrement=True)
    tipolocal = Column(String(100))
    enderecolocal = Column(String(100))
    descricaolocal = Column(String(200))
    nomelocal = Column(String(100))

class Oficina(Base):
    __tablename__ = 'oficina'

    idoficina = Column(Integer, primary_key=True, autoincrement=True)
    tipooficina = Column(String(100))
    descricaooficina = Column(String(200))
    idprojeto = Column(Integer, ForeignKey('celuladeprojetos.idprojeto'))
    dataoficina = Column(Date)
    idlocal = Column(Integer, ForeignKey('localoficina.idlocal'))

class PessoaAuxiliada(Base):
    __tablename__ = 'pessoaauxiliada'

    idpessoa = Column(Integer, primary_key=True, autoincrement=True)
    racapessoa = Column(String(20))
    cpfpessoa = Column(String(14), unique=True, nullable=False)
    nomepessoa = Column(String(100), nullable=False)
    enderecopessoa = Column(String(100))
    rendapessoa = Column(Float)
    sexopessoa = Column(String(50))
    tamanhodafamilia = Column(Integer)
    chavepix = Column(String(100))


# Classes adicionais para especializações e relacionamentos
class Administracao(Base):
    __tablename__ = 'administracao'
    
    idbackoffice = Column(Integer, ForeignKey('backoffice.idbackoffice'), primary_key=True)
    tipo = Column(String(100))

class Marketing(Base):
    __tablename__ = 'marketing'

    idbackoffice = Column(Integer, ForeignKey('backoffice.idbackoffice'), primary_key=True)
    meiodecomunicacao = Column(String(100))

class ProjetosManufaturantes(Base):
    __tablename__ = 'projetosmanufaturantes'

    idprojeto = Column(Integer, ForeignKey('celuladeprojetos.idprojeto'), primary_key=True)
    localestoque = Column(String(100))

class ProjetosNaoManufaturantes(Base):
    __tablename__ = 'projetosnaomanufaturantes'

    idprojeto = Column(Integer, ForeignKey('celuladeprojetos.idprojeto'), primary_key=True)

class ProdutoFisico(Base):
    __tablename__ = 'produtofisico'

    idproduto = Column(Integer, ForeignKey('produto.idproduto'), primary_key=True)
    precoproduto = Column(Float)
    quantidadeproduto = Column(Integer)

class ProdutoDigital(Base):
    __tablename__ = 'produtodigital'

    idproduto = Column(Integer, ForeignKey('produto.idproduto'), primary_key=True)
    linguagem = Column(String(100))
    plataforma = Column(String(100))

class MembroProjeto(Base):
    __tablename__ = 'membroprojeto'

    registrodoaluno = Column(Integer, ForeignKey('membro.registrodoaluno'), primary_key=True)
    idprojeto = Column(Integer, ForeignKey('celuladeprojetos.idprojeto'), primary_key=True)

class ManufaturantesMateriaPrima(Base):
    __tablename__ = 'manufaturantesmateriaprima'
    
    idprojeto = Column(Integer, ForeignKey('celuladeprojetos.idprojeto'), primary_key=True)
    idmateriaprima = Column(Integer, ForeignKey('materiaprima.idmateriaprima'), primary_key=True)

class MateriaPrimaProdutoFisico(Base):
    __tablename__ = 'materiaprimaprodutofisico'

    idmateriaprima = Column(Integer, ForeignKey('materiaprima.idmateriaprima'), primary_key=True)
    idproduto = Column(Integer, ForeignKey('produtofisico.idproduto'), primary_key=True)

class OficinaPessoaAuxiliada(Base):
    __tablename__ = 'oficinapessoaauxiliada'

    idoficina = Column(Integer, ForeignKey('oficina.idoficina'), primary_key=True)
    idpessoa = Column(Integer, ForeignKey('pessoaauxiliada.idpessoa'), primary_key=True)

class ProjetoEdital(Base):
    __tablename__ = 'projetoedital'

    idprojeto = Column(Integer, ForeignKey('celuladeprojetos.idprojeto'), primary_key=True)
    idedital = Column(Integer, ForeignKey('edital.idedital'), primary_key=True)
    datasubmissao = Column(Date)
    dadossubmissao = Column(String(200))

class ProjetosManufaturantesLocal(Base):
    __tablename__ = 'projetosmanufaturanteslocal'

    idprojeto = Column(Integer, ForeignKey('celuladeprojetos.idprojeto'), primary_key=True)
    idlocal = Column(Integer, ForeignKey('localoficina.idlocal'), primary_key=True)

class BackOfficePosts(Base):
    __tablename__ = 'backofficeposts'

    idbackoffice = Column(Integer, ForeignKey('backoffice.idbackoffice'), primary_key=True)
    idpost = Column(Integer, ForeignKey('posts.idpost'), primary_key=True)

class CelulaDeProjetosPosts(Base):
    __tablename__ = 'celuladeprojetosposts'

    idprojeto = Column(Integer, ForeignKey('celuladeprojetos.idprojeto'), primary_key=True)
    idpost = Column(Integer, ForeignKey('posts.idpost'), primary_key=True)

class MembroPosts(Base):
    __tablename__ = 'membroposts'

    idmembro = Column(Integer, ForeignKey('membro.registrodoaluno'), primary_key=True)
    idpost = Column(Integer, ForeignKey('posts.idpost'), primary_key=True)

class PlanilhasBackOfficeMembro(Base):
    __tablename__ = 'planilhasbackofficemembro'
    
    idplanilha = Column(Integer, ForeignKey('planilhas.idplanilha'), primary_key=True)
    idbackoffice = Column(Integer, ForeignKey('backoffice.idbackoffice'), primary_key=True)
    idmembro = Column(Integer, ForeignKey('membro.registrodoaluno'), primary_key=True)
