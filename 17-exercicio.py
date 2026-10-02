import os
os.system("cls")
#SOLICITANDO DADOS

print("===== MENU =====")
print("1 - Hambúrguer - R$ 15,00")
print("2 - Pizza      - R$ 30,00")
print("3 - Sanduíche  - R$ 12,00")
print("4 - Batata     - R$ 45,00")
print("5 - Refrigerante - R$ 5,00")

opcao = int(input("Escolha uma opção: "))

while opcao < 1 or opcao > 5:
    opcao = int(input("Opção inválida! Escolha uma opção de 1 a 5: "))

if opcao == 1:
    print("Você escolheu Hambúrguer - R$ 15,00")
elif opcao == 2:
    print("Você escolheu Pizza - R$ 30,00")
elif opcao == 3:
    print("Você escolheu Sanduíche - R$ 12,00")
elif opcao == 4:
    print("Você escolheu Batata - R$ 45,00")
elif opcao == 5:
    print("Você escolheu Refrigerante - R$ 5,00")