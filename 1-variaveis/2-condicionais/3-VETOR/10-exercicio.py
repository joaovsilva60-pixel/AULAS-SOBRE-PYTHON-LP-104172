import os
os.system("cls")

total = 0
pedidos = []

while True:
    print("\n===== CARDÁPIO =====")
    print("1 - Picanha - R$ 25,00")
    print("2 - Lasanha - R$ 20,00")
    print("3 - Strogonoff - R$ 18,00")
    print("4 - Bife Acebolado - R$ 15,00")
    print("5 - Pão com ovo - R$ 5,00")

    codigo = int(input("Escolha o código do prato: "))

    if codigo == 1:
        prato = "Picanha"
        valor = 25.00
    elif codigo == 2:
        prato = "Lasanha"
        valor = 20.00
    elif codigo == 3:
        prato = "Strogonoff"
        valor = 18.00
    elif codigo == 4:
        prato = "Bife Acebolado"
        valor = 15.00
    elif codigo == 5:
        prato = "Pão com ovo"
        valor = 5.00
    else:
        print("Código inválido!")
        continue

    pedidos.append((prato, valor))
    total += valor

    resposta = input("Deseja escolher outro prato? (s/n): ")

    if resposta.lower() != "s":
        break

print("\n===== RESUMO DO PEDIDO =====")

for prato, valor in pedidos:
    print(f"{prato} - R$ {valor:.2f}")

print(f"\nValor total da conta: R$ {total:.2f}")
