import os
os.system("cls" )
soma = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro positivo (negativo para encerrar): "))

    if numero < 0:
        break

    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"\nA média aritmética dos números informados é: {media:.2f}")
else:
    print("\nNenhum número positivo foi informado.")