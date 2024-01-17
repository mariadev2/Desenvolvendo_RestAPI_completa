from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, RemoverHabilidade
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
     "nome": "Rafael",
     "habilidades":["Python","Flask"]},

    {"nome": "Gabriel",
     "habilidades":["Java","MongoDB"]}

]
class Desenvolvedores(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de id:{id} excluido'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o Adm.'
            response = {'status':'erro','mensagem':mensagem}
        return response

    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados


    def delete(self,id):
        desenvolvedores.pop(id)
        response = {'status': 'sucesso', 'mensagem': 'Registro excluido'}
        return response

    def post(self,id):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        mensagem = 'Registro enviado'
        response = desenvolvedores[posicao], {'status': 'Sucesso', 'mensagem': mensagem}
        return response
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores


api.add_resource(ListaDesenvolvedores,'/dev/')
api.add_resource(Desenvolvedores,'/dev/<int:id>')
api.add_resource(Habilidades,'/habilidades/')
api.add_resource(RemoverHabilidade,'/Editar/<int:id>/')


if __name__ == '__main__':
    app.run(debug=True)