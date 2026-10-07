import os
os.system("cls")
soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))

    soma += nota
    contador += 1

    resposta = input("Deseja inserir mais uma nota? (S/N): ").upper()

    if resposta == "N":
        break

media = soma / contador

print("Quantidade de notas:", contador)
print("Média aritmética:", media)