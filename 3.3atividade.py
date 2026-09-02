import os
os.system('cls')

nome = str(input('Digite seu nome:'))
peso = float(input('Digite seu peso'))
altura =float(input('Digite sua altura'))

IMC=peso /(altura * altura)

if IMC <18.5:
    print(f'IMC:(imc.2f),abaixo do peso')
elif imc<25:
    print(f'IMC:(imc.2f),peso ideal(parabens)')
elif imc < 38:
    print(f'IMC:(imc.2f),obesidade grau I')
elif imc < 35:
    print(f'IMC:(imc.2f),obesidade grau II')
elif imc < 40 :
    print(f'IMC:(imc.2f),obesidade grau III')

