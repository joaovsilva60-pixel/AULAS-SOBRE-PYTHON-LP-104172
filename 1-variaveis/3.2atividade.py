import os
os.system('cls')

nome = str(input('Digite seu nome:'))

primeira_nota = float(input('Digite a primeira nota : '))
segunda_nota = float(input('Digite a segunda nota : '))

media=(primeira_nota + segunda_nota) /2

if media < 4:
    print(f'media:(Media),Reprovado(E)')
elif media < 6:
    print(f'(media):(media),Reprovado(D)')
elif media <7.5:
    print(f'(media):(media),Aprovado(C)')
elif media < 9 :
    print(f'(media):(media),Aprovado(C)')
else:
    print(f'(media):(media),Reprovado(A)')

