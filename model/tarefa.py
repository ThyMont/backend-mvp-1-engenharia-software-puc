from model.base import Base
from sqlalchemy import Column, Integer, String, Boolean


class Tarefa (Base):
    __tablename__ = 'tarefa'

    id = Column("pk_tarefa", Integer, primary_key=True)
    titulo = (Column("titulo", String(30)))
    descricao = (Column("descricao", String(300)))
    feito = (Column("feito", Boolean, default=False))

    def __init__(self, titulo: str, descricao: str = '', id=None, feito=False):
        self.titulo = titulo
        self.descricao = descricao
        self.id = id
        self.feito = feito
