'''
Desafio
'''

while True:
    usuarios = {
        "admin": "1234",
        "rychard": "senha123"
    }

    def login(usuario, senha):
        if usuario in usuarios and usuarios[usuario] == senha:
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorretos.")

    # Exemplo de uso
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    login(usuario, senha)