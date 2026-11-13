import os
os.system('cls')

# Função com parâmetros e retorno
def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2 /2
    return resultado

print('= SOLICITANDO NOTAS =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Chamando a função
soma = calcular_notas(nota1, nota2)

print('\n= EXIBINDO NOTAS =')
print(f'Soma: {soma}')
