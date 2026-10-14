import os
os.system("cls")

nomes = ["João", "Maria", "Pedro", "Ana", "Carlos"]

print('\n= EXIBINDO OS NOMES DO VETOR =')

for indice, nome in enumerate(nomes, start=1):
    print(f'{indice}: {nome}')
