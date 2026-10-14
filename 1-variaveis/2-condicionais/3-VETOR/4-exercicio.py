import os
os.system("cls")

notas = []

for i in range(8):
    nota = float(input(f'Digite a {i + 1}ª nota: '))
    notas.append(nota)

print('\n= EXIBINDO AS NOTAS INFORMADAS =')

for indice, nota in enumerate(notas, start=1):
    print(f'Nota {indice}: {nota}')

#fim do programa
