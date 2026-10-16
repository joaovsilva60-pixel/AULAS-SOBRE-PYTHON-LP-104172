import os
os.system("CLS")
vetor = []


vetor_numeros = []
soma_positivos = 0
quantidade_impares = 0
QUANTIDADE = 5

print('= SOLICITANDO DADOS =')

for i in range(QUANTIDADE):
    numero = int(input(f'Digite o {i+1}º número: '))
    vetor_numeros.append(numero)

    if numero > 0:
        soma_positivos += numero

    if numero % 2 != 0:
        quantidade_impares += 1

print('\n= EXIBINDO DADOS =')
print(f'Soma dos números positivos: {soma_positivos}')
print(f'Quantidade de números ímpares: {quantidade_impares}')
