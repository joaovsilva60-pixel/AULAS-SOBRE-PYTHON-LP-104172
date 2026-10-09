import os
os.system("cls")

pessoas = []

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").upper()
        salario = float(input("Digite o salário: R$ "))

        pessoa = {
            "idade": idade,
            "sexo": sexo,
            "salario": salario
        }

        pessoas.append(pessoa)

        # Limpa o terminal
        import os
        os.system("cls" if os.name == "nt" else "clear")

    elif opcao == 2:
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            # a) Média salarial do grupo
            soma_salarios = sum(p["salario"] for p in pessoas)
            media = soma_salarios / len(pessoas)

            # b) Maior e menor idade
            maior_idade = max(p["idade"] for p in pessoas)
            menor_idade = min(p["idade"] for p in pessoas)

            # c) Mulheres com salário a partir de R$ 5.000
            mulheres = sum(
                1 for p in pessoas
                if p["sexo"] == "F" and p["salario"] >= 5000
            )

            print("\n===== RESULTADOS =====")
            print(f"Média salarial: R$ {media:.2f}")
            print(f"Maior idade: {maior_idade}")
            print(f"Menor idade: {menor_idade}")
            print(
                "Mulheres com salário a partir de "
                f"R$ 5.000,00: {mulheres}"
            )

    elif opcao == 3:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida! Digite 1, 2 ou 3.")