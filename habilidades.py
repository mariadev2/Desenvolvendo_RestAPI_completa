import json

from flask_restful import Resource
from flask import request

lista_habilidades = ['Python','Java','PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)

        if dados in lista_habilidades:
            mensagem = f'Registro já existe!{lista_habilidades}'

        elif dados not in lista_habilidades:
            lista_habilidades.append(dados)
            mensagem = f'Registro Salvo!{lista_habilidades}'
        return mensagem


class RemoverHabilidade(Resource):
    def delete(self,id):

        try:
            lista_habilidades.pop(id)
            mensagem = f'Registro Excluido!{lista_habilidades}'

        except IndexError:
            mensagem = 'Registro não encontrado!'

        return mensagem

    def put(self,id):
        try:
            dados = json.loads(request.data)
            lista_habilidades[id] = dados
            mensagem = 'Editado!'

        except IndexError:
            mensagem = 'ID nao encontrado'

        return mensagem

