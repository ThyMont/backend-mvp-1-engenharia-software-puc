from flask_openapi3 import Info, OpenAPI, Tag
from flask import redirect, Response
from typing import Annotated
from flask_cors import CORS
from functools import wraps


from schemas.tarefa import NovaTarefaForm, TarefaViewSchema, ListaTarefasSchema, TarefaPath, TarefaDelSchema
from schemas.error import ErrorSchema

from services.tarefa import TarefaService

info = Info(title='Tarefa_API', version='1.0.0')
app = OpenAPI(__name__, info=info)
CORS(app)


def returns_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        r = f(*args, **kwargs)
        return Response(*r, content_type='application/json; charset=utf-8')
    return decorated_function


# Tags
home_tag = Tag(
    name="Docs", description="Documentação da aplicação: Swagger, Redoc ou RapiDoc")
tarefa_tag = Tag(name="Tarefa", description="Referente a tarefas")


@app.get('/', tags=[home_tag])
@app.get('/home', tags=[home_tag])
@app.get('/index', tags=[home_tag])
def home():
    """
    Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/tarefas', tags=[tarefa_tag], responses={"200": TarefaViewSchema, "400": ErrorSchema})
@returns_json
def criar_tarefa(form: NovaTarefaForm):
    """
    Cria uma nova tarefa
    """
    print(form)
    service = TarefaService()
    return service.criar(form)


@app.get('/tarefas', tags=[tarefa_tag], responses={"200": ListaTarefasSchema, "400": ErrorSchema})
@returns_json
def listar_tarefas():
    """
    lista todas as tarefas
    """
    service = TarefaService()
    lista = service.listar()
    return lista


@app.put('/tarefas/check/<int:id>', tags=[tarefa_tag], responses={"200": TarefaDelSchema, "400": ErrorSchema})
@returns_json
def alterar_feito(path: TarefaPath):
    service = TarefaService()
    retorno = service.alterar_feito(path.id)
    return retorno


@app.delete('/tarefas/<int:id>', tags=[tarefa_tag], responses={"200": TarefaDelSchema, "400": ErrorSchema})
def deletar_tarefa(path: TarefaPath):
    service = TarefaService()
    retorno = service.apagar(path.id)
    return retorno


if __name__ == '__main__':
    app.run(debug=True)
