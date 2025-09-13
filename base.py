from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def get_dados():
    with open('Dados.json', 'r', encoding='utf-8')as f:
        dados = json.load(f)
    return dados


def put_dados(dados):
    with open('Dados.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4)


@app.route('/livros', methods=['GET'])
def GET_livros():
    dados = get_dados()
    return jsonify(dados['livros'])


@app.route('/livros', methods=['POST'])
def POST_livros():
    dados = get_dados()
    dados['livros'].append(request.get_json())

    put_dados(dados)

    return request.get_json(), 201


@app.route('/livros', methods=['PUT'])
def PUT_livros():
    dados = get_dados()
    #fazer depois de definir os campos do arquivo
    
    return jsonify({"msg": "Método ainda não implementado"}), 501


@app.route('/livros', methods=['PATCH'])
def PATCH_livros():
    dados = get_dados()
    #fazer depois de definir os campos do arquivo

    return jsonify({"msg": "Método ainda não implementado"}), 501


@app.route('/livros', methods=['DELETE'])
def DELETE_livros():
    dados = get_dados()


    return jsonify({"msg": "Método ainda não implementado"}), 501



if __name__ == '__main__':
    app.run(debug=True)