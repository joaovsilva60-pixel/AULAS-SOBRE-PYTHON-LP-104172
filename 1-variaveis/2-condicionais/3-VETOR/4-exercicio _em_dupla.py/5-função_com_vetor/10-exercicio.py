import os
os.system("cls")

def ler_nota():
    while True:
        nota = float(input("Digite uma nota (0 a 10): "))

        if nota >= 0 and nota <= 10:
            return nota
        else:
            print("Nota inválida! Digite entre 0 e 10.")


def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media


def verificar_aprovacao(media):
    if media >= 7:
        print("Aluno APROVADO!")
    else:
        print("Aluno REPROVADO!")


# Programa principal
print("=== MÉDIA DO ALUNO ===")

nota1 = ler_nota()
nota2 = ler_nota()

media = calcular_media(nota1, nota2)

print("\nNota 1:", nota1)
print("Nota 2:", nota2)
print("Média:", media)

verificar_aprovacao(media)
