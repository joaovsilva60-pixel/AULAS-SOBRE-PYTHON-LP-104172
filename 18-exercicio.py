import os
os.system ("cls")
#EXIBINDO DADOS

login_correto = "admin"
senha_correta = "1234"

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

while login != login_correto or senha != senha_correta:
    print("Login ou senha incorretos!")
    
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

print("Login realizado com sucesso!")