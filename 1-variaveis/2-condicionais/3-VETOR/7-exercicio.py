import os
os.system("cls")

print('=== INSERINDO NÚMEROS NO VETOR ===')

vetor_numeros = []
QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f'Digite o {i+1}º número: '))
    vetor_numeros.append(numero)

print('\n=== NÚMEROS INFORMADOS ===')

for posicao, numero in enumerate(vetor_numeros, start=1):
    print(f'{posicao}º número: {numero}')

menor = min(vetor_numeros)
maior = max(vetor_numeros)

print(f'\nMenor número: {menor}')
print(f'Maior número: {maior}')
