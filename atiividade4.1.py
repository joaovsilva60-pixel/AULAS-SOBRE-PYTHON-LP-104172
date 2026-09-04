import os
os.system('cls')


#SOLICITANDO DADOS
login=input('Digite seu login: ')
senha=input('Digite sua senha')

#PROCESSAMENTO
login_salvo ="joao"
senha_salva="080808"

login_estar_correto = login ==login_salvo
senha_estar_correto = senha == senha_salva


#SAIDA
if login_estar_correto and senha_estar_correto:
    print('Bem Vindo!')
else:
    print('Login ou senha invalidos')




