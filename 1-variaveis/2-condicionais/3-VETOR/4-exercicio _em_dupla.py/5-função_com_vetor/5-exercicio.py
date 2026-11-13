import os
os.system("cls")
def converter_metros(metros):
    centimetros = metros * 100
    return centimetros


# Programa principal
valor = float(input("Digite o valor em metros: "))

resultado = converter_metros(valor)

print("O valor em centímetros é:", resultado, "cm")