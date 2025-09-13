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
    novo_livro = request.get_json()
    dados['livros'].append(novo_livro)

    put_dados(dados)

    return jsonify(novo_livro), 201


@app.route('/livros/<int:id>', methods=['PUT'])
def PUT_livros(id):
    dados = get_dados()
    livros = dados['livros']
    novo_livro = request.get_json()
    livro_filtrado = {}
    chaves = ["id", "titulo", "autor", "ano", "preco"]

    for x in chaves:
        if x not in novo_livro:
            return jsonify({"Erro": f"Chave {x} ausente"}), 400
        livro_filtrado[x] = novo_livro[x]
    
    for i, livro in enumerate(livros):
        if livro["id"] == id:
            livros[i] = livro_filtrado
            put_dados(dados)
            return jsonify(livro_filtrado), 200
        
    return jsonify({"Erro": "Livro não encontrado"}), 404


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