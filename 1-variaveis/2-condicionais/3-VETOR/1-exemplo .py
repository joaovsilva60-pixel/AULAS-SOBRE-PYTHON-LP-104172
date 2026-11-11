import os
os.system("cls")


# Criando uma função
def cabecalho():
    print('\n')
    print('='*15)
    print('     SENAI')
    print('='*15)

# Solicitando o nome
cabecalho()
nome = input('Digite seu nome: ')

# Solicitando a idade
cabecalho()
idade = input('Digite sua idade: ')

# Exibindo os dados
cabecalho()
print(f'Nome: {nome}')
print(f'Idade: {idade}')

import os

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
