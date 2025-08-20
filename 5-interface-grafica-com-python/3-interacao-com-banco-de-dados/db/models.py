from sqlalchemy import Column, Float, Integer, String
from db.database import Base


class Agenda(Base):
    __tablename__ = "agenda"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    telefone = Column(String(length=12), nullable=False)


class Produto(Base):
    __tablename__ = "produto"

    codigo = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float(precision=2), nullable=False)
