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

@app.route('/livros/<int:id>', methods=['GET'])
def GET_livro(id):
    dados = get_dados()
    livros = dados['livros']

    for livro in livros:
        if livro["id"] == id:
            return jsonify(livro), 200

    return jsonify({"Erro": "Livro não encontrado"}), 404


@app.route('/livros', methods=['POST'])
def POST_livros():
    dados = get_dados()
    livros = dados['livros']
    novo_livro = request.get_json()
    chaves = ["titulo", "autor", "ano", "generos", "preco"]
    livro_filtrado = {}
    ausentes = []

    for x in chaves:
        if x not in novo_livro:
            ausentes.append(x)
        else:
            livro_filtrado[x] = novo_livro[x]
    if ausentes:
        return jsonify({"Erro": f"Chaves ausentes: {ausentes}"}), 400

    if livros:
        max_id = max(l["id"] for l in livros)
    else:
        max_id = 0
    livro_filtrado["id"] = max_id + 1

    livros.append(livro_filtrado)
    put_dados(dados)

    return jsonify(livro_filtrado), 201


@app.route('/livros/<int:id>', methods=['PUT'])
def PUT_livros(id):
    dados = get_dados()
    livros = dados['livros']
    novo_livro = request.get_json()
    livro_filtrado = {}
    chaves = ["id", "titulo", "autor", "ano", "generos", "preco"]
    ausentes = []

    for x in chaves:
        if x not in novo_livro:
            ausentes.append(x)
        else:
            livro_filtrado[x] = novo_livro[x]
    if ausentes:
        return jsonify({"Erro": f"Chaves ausentes: {ausentes}"}), 400
    
    for i, livro in enumerate(livros):
        if livro["id"] == id:
            livros[i] = livro_filtrado
            put_dados(dados)
            return jsonify(livro_filtrado), 200
        
    return jsonify({"Erro": "Livro não encontrado"}), 404


@app.route('/livros/<int:id>', methods=['PATCH'])
def PATCH_livros(id):
    dados = get_dados()
    livros = dados['livros']
    novo_livro = request.get_json()
    
    for i, livro in enumerate(livros):
        if livro["id"] == id:
            for chave, valor in novo_livro.items():
                if chave in livro:
                    livros[i][chave] = valor
            put_dados(dados)
            return jsonify(livros[i]), 200

    return jsonify({"Erro": "Livro não encontrado"}), 404


@app.route('/livros/<int:id>', methods=['DELETE'])
def DELETE_livros(id):
    dados = get_dados()
    livros = dados["livros"]

    for i, livro in enumerate(livros):
        if livro["id"] == id:
            deletado = livros.pop(i)
            put_dados(livros)
            return jsonify(deletado), 200
    
    return jsonify({"Erro": "Livro não encontrado"}), 404



if __name__ == '__main__':
    app.run(debug=True)