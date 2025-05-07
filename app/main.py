from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = {}


@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.get_json()
    cpf = dados.get("cpf")

    if cpf in usuarios:
        return jsonify({"erro": "Usuário já existe"}), 400

    usuarios[cpf] = {
        "nome": dados.get("nome"),
        "email": dados.get("email"),
        "senha": dados.get("senha"),
        "cpf": cpf
    }

    return jsonify({"mensagem": "Usuário criado com sucesso"}), 201


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(list(usuarios.values())), 200


@app.route("/usuarios/<cpf>", methods=["GET"])
def buscar_usuario(cpf):
    usuario = usuarios.get(cpf)

    if usuario:
        return jsonify(usuario), 200

    return jsonify({"erro": "Usuário não encontrado"}), 404


@app.route("/usuarios/<cpf>", methods=["DELETE"])
def deletar_usuario(cpf):
    if cpf in usuarios:
        del usuarios[cpf]
        return jsonify({"mensagem": "Usuário deletado com sucesso"}), 200

    return jsonify({"erro": "Usuário não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
