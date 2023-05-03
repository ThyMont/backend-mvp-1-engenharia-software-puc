from pydantic import BaseModel, Field
from typing import List

from model.tarefa import Tarefa


class TarefaViewSchema(BaseModel):
    '''
    Apresentação de uma tarefa
    '''
    id: int = 1
    titulo: str = 'Consulta'
    descricao: str = 'Dermatorlogista dia 02/03/2023'
    feito: bool = False


class NovaTarefaForm(BaseModel):
    """
    Formulário para criação de uma nova tarefa
    """
    titulo: str = 'Consulta'
    descricao: str = 'Dermatorlogista dia 02/03/2023'


class TarefaPath(BaseModel):
    """
    Formulário para criação de uma nova tarefa
    """
    id: int = Field(1, description='ID da tarefa')


class UpdateTarefaSchema(BaseModel):
    '''
    Apresentação de uma tarefa
    '''
    id: int = 1
    titulo: str = 'Consulta - Dermatologista'
    descricao: str = 'Consulta com o Dr. Danillo no dia 04/03/2023'
    feito: bool = False


class ListaTarefasSchema(BaseModel):
    """
    Apresenta uma lista de tarefas
    """
    lista: List[NovaTarefaForm] = []
    quantidade: int = len(lista)


class TarefaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str


def apresenta_tarefa(tarefa: Tarefa):
    view = TarefaViewSchema()
    view.id = tarefa.id
    view.titulo = tarefa.titulo
    view.descricao = tarefa.descricao
    view.feito = tarefa.feito
    return view


def apresenta_lista_tarefa(lista: list):
    result = []
    for tarefa in lista:
        result.append(apresenta_tarefa(tarefa))
    listaView = ListaTarefasSchema()
    listaView.quantidade = len(result)
    listaView.lista = result.copy()
    return listaView
