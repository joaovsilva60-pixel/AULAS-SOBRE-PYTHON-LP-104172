import os
os.system("cls")

def calcular_media(notas):
    media = sum(notas) / len(notas)
def mostrar_resultado(media,lista_de_notas):
    print('\n=Exibindo NOTAS=')
    for nota in lista_de_notas:
        print(f'Nota:{nota}')
        
        print(f'\nMedia:{media}')

# Programa principal
vetor = []

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    vetor.append(nota)

media = calcular_media(vetor)

print("\nNotas do aluno:", vetor)
print("Média do aluno:", media)