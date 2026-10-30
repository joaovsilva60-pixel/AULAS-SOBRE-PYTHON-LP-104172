import os
os.system("cls")
pacientes = []

while True:
    print("\n===== SISTEMA DE CADASTRO DE PACIENTES =====")
    print("1 - Cadastrar paciente")
    print("2 - Listar pacientes")
    print("3 - Atualizar paciente")
    print("4 - Remover paciente")
    print("5 - Buscar paciente")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do paciente: ")
        sobrenome = input("Digite o sobrenome do paciente: ")

        paciente = {
            "nome": nome,
            "sobrenome": sobrenome
        }

        pacientes.append(paciente)
        print("Paciente cadastrado com sucesso!")

    elif opcao == "2":
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            print("\n===== LISTA DE PACIENTES =====")

            for i, paciente in enumerate(pacientes):
                print(
                    f"{i + 1} - {paciente['nome']} "
                    f"{paciente['sobrenome']}"
                )

    elif opcao == "3":
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            for i, paciente in enumerate(pacientes):
                print(
                    f"{i + 1} - {paciente['nome']} "
                    f"{paciente['sobrenome']}"
                )

            try:
                numero = int(input("Digite o número do paciente: "))

                if 1 <= numero <= len(pacientes):
                    nome = input("Digite o novo nome: ")
                    sobrenome = input("Digite o novo sobrenome: ")

                    pacientes[numero - 1]["nome"] = nome
                    pacientes[numero - 1]["sobrenome"] = sobrenome

                    print("Paciente atualizado com sucesso!")
                else:
                    print("Número de paciente inválido.")

            except ValueError:
                print("Digite um número válido.")

    elif opcao == "4":
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            for i, paciente in enumerate(pacientes):
                print(
                    f"{i + 1} - {paciente['nome']} "
                    f"{paciente['sobrenome']}"
                )

            try:
                numero = int(input("Digite o número do paciente que deseja remover: "))

                if 1 <= numero <= len(pacientes):
                    removido = pacientes.pop(numero - 1)
                    print(
                        f"Paciente {removido['nome']} "
                        f"{removido['sobrenome']} removido com sucesso!"
                    )
                else:
                    print("Número de paciente inválido.")

            except ValueError:
                print("Digite um número válido.")

    elif opcao == "5":
        busca = input("Digite o nome ou sobrenome do paciente: ").strip().lower()

        encontrados = [
            paciente for paciente in pacientes
            if busca in paciente["nome"].lower()
            or busca in paciente["sobrenome"].lower()
        ]

        if encontrados:
            print("\n===== PACIENTES ENCONTRADOS =====")

            for paciente in encontrados:
                print(f"{paciente['nome']} {paciente['sobrenome']}")
        else:
            print("Nenhum paciente encontrado.")

    elif opcao == "6":
        print("Programa encerrado. Até logo!")
        break

    else:
        print("Opção inválida! Escolha uma opção de 1 a 6.")
