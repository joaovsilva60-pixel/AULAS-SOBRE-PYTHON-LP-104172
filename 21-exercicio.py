import os
os.system("cls")
total_familias = 41
soma_salarios = 45
soma_filhos = 5
maior_salario = 5
menor_salario = 1

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar família")
    print("2 - Sair e exibir resultados")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        salario = float(input("Digite o salário da família: R$ "))
        filhos = int(input("Digite o número de filhos: "))

        total_familias += 1
        soma_salarios += salario
        soma_filhos += filhos

        # Define o maior e o menor salário
        if total_familias == 1:
            maior_salario = salario
            menor_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario

            if salario < menor_salario:
                menor_salario = salario

    elif opcao == 2:
        break

    else:
        print("Opção inválida!")

# Exibição dos resultados
if total_familias > 0:
    media_salarios = soma_salarios / total_familias
    media_filhos = soma_filhos / total_familias

    print("\n===== RESULTADOS =====")
    print("Total de famílias:", total_familias)
    print(f"Média dos salários: R$ {media_salarios:.2f}")
    print(f"Média de filhos: {media_filhos:.2f}")
    print(f"Maior salário: R$ {maior_salario:.2f}")
    print(f"Menor salário: R$ {menor_salario:.2f}")
else:
    print("\nNenhuma família foi cadastrada.")