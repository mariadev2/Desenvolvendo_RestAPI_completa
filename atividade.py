import json

from flask import Flask,jsonify,request
app = Flask(__name__)

lista_tarefas = [
    {
    "id":0,
    "Responsavel": "Maria Eduarda",
     "Tarefa": "Retirar lixo da cozinha",
     "Status": "Feito"}
]
@app.route("/lista/visualizar/", methods = ['GET'])
def listar_tarefas():
    return jsonify(lista_tarefas)

@app.route("/lista/adicionar/", methods = ['POST'])
def adicionar_tarefas():
    dados = json.loads(request.data)
    lista_tarefas.append(dados)
    mensagem = "Tarefa adicionada!"
    return jsonify(mensagem)

@app.route("/lista/editar/<int:id>/", methods = ['POST'])
def editar_tarefa(id):
    dados = json.loads(request.data)

    if id in lista_tarefas:
        lista_tarefas[id]["Status"].update(dados)
        mensagem = "Tarefa Editada!"
    else:
        mensagem = "Id não encontrado"
    return jsonify(mensagem)

@app.route("/lista/deletar/<int:id>/", methods = ['DELETE'])
def deletar_tarefas(id):
    lista_tarefas.pop(id)
    mensagem = "Tarefa Excluida!"
    return jsonify(mensagem)

if __name__ == "__main__":
    app.run()