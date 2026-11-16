import os
os.system("cls")


def inflacionar(preco):
    if preco < 100:
        resultado = preco * 1.10
    else:
        resultado = preco * 1.20

    return resultado


# Programa principal
preco = float(input("Digite o preço do produto: R$ "))

novo_preco = inflacionar(preco)

print(f"Preço original: R$ {preco:.2f}")
print(f"Preço com inflação: R$ {novo_preco:.2f}")
