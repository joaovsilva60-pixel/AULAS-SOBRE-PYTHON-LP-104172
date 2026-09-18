import os
os.system("cls") 

# SOLICITANDO DADOS (Nomes corrigidos para coincidir com os cálculos)
primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))

# PROCESSAMENTO
media = (primeiro_numero + segundo_numero) / 2
soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

# EXIBIÇÃO DOS RESULTADOS
if primeiro_numero == segundo_numero:
    print("Os dois numeros sao iguais!")

print("Média:", media)
print("Soma:", soma)
print("Produto:", produto)
print("Maior:", maior)
print("Menor:", menor)




