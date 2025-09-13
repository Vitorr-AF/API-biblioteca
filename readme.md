# API de Livros com Flask

Essa é uma API REST simples para gerenciamento de livros, construída em **Python** usando **Flask** e um arquivo JSON como "banco de dados".

---

## Funcionalidades

A API permite:

- **GET /livros** → Retorna todos os livros  
- **GET /livros/<id>** → Retorna um livro específico pelo ID  
- **POST /livros** → Cria um novo livro (o ID é gerado automaticamente)  
- **PUT /livros/<id>** → Atualiza completamente um livro existente  
- **PATCH /livros/<id>** → Atualiza parcialmente um livro existente  
- **DELETE /livros/<id>** → Remove um livro pelo ID  

Todos os endpoints retornam **JSON** e códigos de status HTTP apropriados (`200`, `201`, `400`, `404`).

---

## Estrutura do JSON (`Dados.json`)

```json
{
    "livros": [
        {
            "id": 1,
            "titulo": "Python Avançado",
            "autor": "John Python",
            "ano": 2025,
            "generos": ["programação", "tecnologia"],
            "preco": 120.50
        }
    ]
}
```

---

## Como rodar

1. Instale as dependências:
```bash
pip install flask
```

2. Execute a API:
```bash
python base.py
```

3. Acesse os endpoints via **Postman**, **curl** ou outro cliente HTTP.

---

## Observações

- O arquivo `Dados.json` é atualizado a cada operação de criação, atualização ou exclusão de livros.  
- O POST gera automaticamente o `id` do novo livro.  
- PUT exige todos os campos obrigatórios (`id`, `titulo`, `autor`, `ano`, `generos`, `preco`).  
- PATCH permite atualizar apenas os campos desejados.  
- DELETE remove o livro e retorna os dados excluídos.

---

## Melhorias futuras

- Mais funções serão adicionadas futuramente

