import os
os.system("cls")
login_correto = "admin"
senha_correta = "1234"

tentativas = 0
acesso = False

while tentativas < 3:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    tentativas += 1

    if login == login_correto and senha == senha_correta:
        print("Login e senha corretos! Acesso permitido.")
        acesso = True
        break
    else:
        print("Login ou senha incorretos.")

if not acesso:
    print("Número máximo de tentativas atingido. Programa finalizado.")