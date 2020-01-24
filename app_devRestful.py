from flask import Flask, request
from flask_restful import Resource, Api
import json
from skills import skills
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

api = Api(app)

class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Contate o Administrador da Rede.'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response
        #return {'nome:' : 'Rodrigo Vieira'}
    def put(self, id):
        dados = json.loads ( request.data )
        developers[id] = dados
        return dados
        #return {'nome:' : 'Rodrigo Vieira'}
    def delete(self, id):
        developers.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro Excluido!'}
        #return {'nome:' : 'Rodrigo Vieira'}
    def post(self):
        return {'nome:' : 'Rodrigo Vieira'}

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class list_developers(Resource):
    def get(self):
        return developers

    def post(self):
        dados = json.loads(request.data)
        posit = len(developers)
        dados['id'] = posit
        developers.append(dados)
        return (developers[posit])

api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(list_developers, '/dev/')
api.add_resource(skills, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)
