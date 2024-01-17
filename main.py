from flask import Flask, jsonify, request
import json

app = Flask(__name__)
desenvolvedores = [
    {
     "nome": "Rafael",
     "habilidades":["Python","Flask"]},

    {"nome": "Gabriel",
     "habilidades":["Java","MongoDB"]}

]
@app.route("/dev/<int:id>/", methods = ['GET','PUT','DELETE'])

def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de id:{id} excluido'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o Adm.'
            response = {'status':'erro','mensagem':mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro excluido'})

@app.route("/dev/",methods = ['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        mensagem = 'Registro enviado'
        return jsonify(desenvolvedores[posicao],{'status':'Sucesso','mensagem':mensagem})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == "__main__":
    app.run()