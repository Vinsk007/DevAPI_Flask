from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {
        'id': '0',
        'nome': 'Rodrigo',
        'diplomas': ['Engenheiro Quimico', 'Engenheiro de Instrumentacao']
    },
    {
        'id': '1',
        'nome': 'Vieira',
        'Programacao': ['Python', 'VBA Excel']
    }
]

# Devolve um desenvolvedor pelo ID, e também altera e deleta um desenvolvedor via POSTMAN
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developer (id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Contate o Administrador da Rede.'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        developers[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro Excluido!'})

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['GET', 'POST'])
def list_developers():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posit = len(developers)
        dados['id'] = posit
        developers.append(dados)
        return jsonify(developers[posit])
        #return jsonify ( {'status': 'sucesso', 'mensagem': 'Registro Incluido!'} )
    elif request.method == 'GET':
        return jsonify(developers)

if __name__ == '__main__':
    app.run(debug=True)