import os
os.system("cls")

def logo_senai():
    os.system('cls')
    print('\n================')
    print('   SENAI - BAHIA')
    print('================')

def mostrar_dados(nome, email, telefone):
    print(f'Nome: {nome}')
    print(f'E-mail: {email}')
    print(f'Telefone: {telefone}')

print('= SOLICITANDO DADOS =')

logo_senai()
nome = input('Digite seu nome: ')

logo_senai()
email = input('Digite seu email: ')

logo_senai()
telefone = input('Digite seu telefone: ')

logo_senai()
print('\n= EXIBINDO DADOS =')
mostrar_dados(nome, email, telefone)
