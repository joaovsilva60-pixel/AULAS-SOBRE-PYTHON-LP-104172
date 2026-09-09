import os
os .system('cls')

resultado=0

primeiro_numero = float(input('Digite o primeiro numero'))
segundo_numero = float(input('Digite o segundo numero'))
operador = input("Digite o operador(+ - * /).  ")

#PROCESSANDO
match operador:
    case'+':
        resultado  = primeiro_numero +segundo_numero
    case'-':
        resultado  = primeiro_numero - segundo_numero
    case'*':
        resultado  = primeiro_numero * segundo_numero
    case'/':
        resultado  = primeiro_numero / segundo_numero
if segundo_numero !=0:
    resultado =primeiro_numero /segundo_numero
else:
    resultado ="ERRO !Não é possivel dividir por zero"
valido=False
case_'
resultado ="Operador invalido!"
valido =False

#SAIDA
print("\n=RESUMO DA OPERAÇÃO =")
print(f"Primeiro numero:(primeiro_numero)")
print(f"segundo numero:(segundo_numero)")

if valido:
    print(f"Resultado :(resultado:.2f)")
else:
    print(f"Resultado:(resultado)")


