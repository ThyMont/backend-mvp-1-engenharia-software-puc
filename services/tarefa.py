from model import Session
from model.tarefa import Tarefa

from schemas.tarefa import NovaTarefaForm, TarefaViewSchema, ListaTarefasSchema, TarefaPath, TarefaDelSchema, apresenta_tarefa, apresenta_lista_tarefa


class TarefaService ():
    def criar(_, form: NovaTarefaForm):
        try:
            tarefa = Tarefa(titulo=form.titulo, descricao=form.descricao)
            session = Session()
            session.add(tarefa)
            session.commit()
            print(tarefa)
            return apresenta_tarefa(tarefa).json(), 200

        except Exception as e:
            msg = "Não foi possível completar esta ação"
            return {'msg': msg}, 400

    def alterar_feito(_, id):
        session = Session()
        try:
            tarefa = tarefa = session.query(
                Tarefa).filter(Tarefa.id == id).first()
            if tarefa:
                session.query(Tarefa).filter(Tarefa.id == id).update(
                    {Tarefa.feito: not tarefa.feito})
                session.commit()
                return apresenta_tarefa(tarefa).json(), 200
            else:
                return {'msg': 'Tarefa não encontrada'}, 404
        except:
            return {'msg': "Não foi possível completar esta ação"}, 400

    def apagar(_, id):
        session = Session()
        tarefa = session.query(Tarefa).filter(Tarefa.id == id).first()
        quant = session.query(Tarefa).filter(Tarefa.id == id).delete()

        session.commit()
        if quant:
            return {'mensagem':  "Tarefa '" + tarefa.titulo+"' excluída com sucesso"}
        else:
            msg = "Tarefa não encontrada"
        return {'mensagem': msg}, 404

    def listar(_):
        try:
            session = Session()
            lista = session.query(Tarefa).order_by(Tarefa.feito).all()
            return apresenta_lista_tarefa(lista).json(), 200

        except Exception as e:
            msg = "Não foi possível completar esta ação"
            raise e
            # return {'msg': msg}, 400
