
import os
os.system('cls')

print('= INSERINDO NÚMEROS NO VETOR =')

vetor_numeros = []
numero=int(input("digite um numero :"))
vetor_numeros.append(5)
numero=int(input("digite um numero :"))
vetor_numeros.append(10)
numero=int(input("digite um numero :"))
vetor_numeros.append(15)
numero=int(input("digite um numero :"))
vetor_numeros.append(20)
numero=int(input("digite um numero :"))
vetor_numeros.append(25)
numero=int(input("digite um numero :"))

print('\n= MOSTRANDO NÚMEROS DO VETOR =')
print(f'Primeira posição do vetor: {vetor_numeros[0]}')

# SUA VEZ, MOSTRE A ÚLTIMA POSIÇÃO DO VETOR.
print(f'Última posição do vetor: {vetor_numeros[-1]}')