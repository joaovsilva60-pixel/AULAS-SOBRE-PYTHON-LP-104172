import os
os.system

matricula =input('digite a matricula :')
ano_de_nascimento= int(input("digite o ano de nascimento:"))
tempo_de_trabalho =float(input('digite o tempo de trabalho'))

idade= date.today().year - ano_de_nascimento

if idade >= 65 or tempo_de_trabalho >=30:
    resultado ='Requer aposentadoria.'
else:
    resultado ='Não requerer aposentadoria.'

    print(f'Resultado:{resultado}')
    print(f'data: {'Date.today()}')