import os
os.system("cls")
pares = 0
impares = 0
soma_pares = 0
soma_total = 0
total_numeros = 0

while True:
    numero = int(input("Digite um número positivo (0 para encerrar): "))

    if numero == 0:
        break

    if numero % 2 == 0:
        pares += 1
        soma_pares += numero
    else:
        impares += 1

    soma_total += numero
    total_numeros += 1

# Resultados
print("\n===== RESULTADOS =====")
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)

if pares > 0:
    media_pares = soma_pares / pares
    print(f"Média dos valores pares: {media_pares:.2f}")
else:
    print("Nenhum número par foi informado.")

if total_numeros > 0:
    media_geral = soma_total / total_numeros
    print(f"Média geral dos números: {media_geral:.2f}")
else:
    print("Nenhum número foi informado.")