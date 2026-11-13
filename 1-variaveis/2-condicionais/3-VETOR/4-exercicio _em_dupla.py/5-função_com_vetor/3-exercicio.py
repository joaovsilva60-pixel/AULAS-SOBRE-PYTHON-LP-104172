import os
os.system("cls")

def verificar_numero(numero):
    if numero > 0:
        return "Número positivo"
    elif numero < 0:
        return "Número negativo"
    else:
        return "O número é zero"


# Programa principal
valor = int(input("Digite um número inteiro: "))

resultado = verificar_numero(valor)

print(resultado)