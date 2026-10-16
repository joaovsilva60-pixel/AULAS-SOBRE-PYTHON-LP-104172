import os
os.system("CLS")

vetor = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

print("Ordem digitada:", vetor)
print("Ordem inversa:", vetor[::-1])
