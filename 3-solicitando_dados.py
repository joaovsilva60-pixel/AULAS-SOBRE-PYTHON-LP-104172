import os

#limpa o terminal
os .system ("cls")

#SOLICITANDO DADOS.
#intput adiciona o que for digitado no terminal na variavel como texto.
nome=input('Digite seu nome:')
sobrenome=input('Digite seu sobrenome:')
idade=int(input('Digite sua idade:'))
peso=float(input('Digite seu peso:'))
altura=float(input('Digite sua altura'))

#int()coverte o que foi  digitado em inteiro (números inteiros)

#float()converte o que foi digitado e, float(números reais)


#MOSTRANDO DADOS.
print('Nome:',nome) 
print('Sobrenome: ', sobrenome)
print('Idade: ', idade) 
print('Peso: ', peso)   
