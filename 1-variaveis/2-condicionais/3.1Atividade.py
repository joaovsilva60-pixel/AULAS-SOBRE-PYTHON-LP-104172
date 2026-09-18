import os
os.system('cls')

#SOLICITANDO DADOS
nome = str(input("Digite seu nome:"))

quant_de_macas = int(input("Digite a quantidade de macas: "))

if quant_de_macas < 12:
    maca = quant_de_macas *  1.3
else:
    maca = quant_de_macas

print('\n = EXIBINDO DADOS =')
input(f'valor total da compra:{maca:.2f}')