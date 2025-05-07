from app.main import app, usuarios

def test_criar_usuario():
    with app.test_client() as client:
        usuarios.clear()
        resposta = client.post("/usuarios", json={
            "nome": "João",
            "email": "joao@example.com",
            "senha": "123456",
            "cpf": "11111111111"
        })
        assert resposta.status_code == 201

def test_listar_usuarios():
    with app.test_client() as client:
        usuarios.clear()
        client.post("/usuarios", json={
            "nome": "Maria",
            "email": "maria@example.com",
            "senha": "123456",
            "cpf": "22222222222"
        })
        resposta = client.get("/usuarios")
        assert resposta.status_code == 200
        assert type(resposta.get_json()) == list

def test_buscar_usuario():
    with app.test_client() as client:
        usuarios.clear()
        client.post("/usuarios", json={
            "nome": "Carlos",
            "email": "carlos@example.com",
            "senha": "123456",
            "cpf": "33333333333"
        })
        resposta = client.get("/usuarios/33333333333")
        assert resposta.status_code == 200
        assert resposta.get_json()["nome"] == "Carlos"

def test_deletar_usuario():
    with app.test_client() as client:
        usuarios.clear()
        client.post("/usuarios", json={
            "nome": "Ana",
            "email": "ana@example.com",
            "senha": "123456",
            "cpf": "44444444444"
        })
        resposta = client.delete("/usuarios/44444444444")
        assert resposta.status_code == 200
