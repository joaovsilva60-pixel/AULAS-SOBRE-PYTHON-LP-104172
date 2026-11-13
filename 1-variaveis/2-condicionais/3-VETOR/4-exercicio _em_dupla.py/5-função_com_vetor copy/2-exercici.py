import os
os.system('cls')

# Função para verificar se o número é par ou ímpar
def verificar_numero(numero):
    if numero % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Ímpar'

    return resultado


# Criando o vetor
numeros = []

print('= VERIFICANDO NÚMEROS =')

for i in range(5):
    numero = int(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)

print('\n= RESULTADO =')

for numero in numeros:
    situacao = verificar_numero(numero)
    print(f'Número: {numero} - {situacao}')
