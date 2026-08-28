import os
os.system('cls')

numero = int(input('Digite a idade: '))

if numero < 16:
    print('nao vota!')
elif 16 <= numero < 18 or numero > 65:
    print("voto opcional")
else:
    print("voto obrigatorio")
