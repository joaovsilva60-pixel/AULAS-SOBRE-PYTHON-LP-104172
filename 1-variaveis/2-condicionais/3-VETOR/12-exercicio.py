import os

lista_series = []

while True:
    os.system("cls")

    print('''
===MERCADO DENDEIZEIROS ===
1-  CADASTRAR Serie
2-  LISTAR serie
3-  sAIR
    ''''')
    opcao = input('Escolha uma opção: ')
    match opcao:
        case '1':
            
            nome = input('Digite o nome da série: ').strip().upper()

            lista_series.append(nome)
            print(f'Série  cadastrada com sucesso!')
            input('Pressione Enter para continuar...')
        case '2':
            print('=== LISTAR SERIES ===')
            if len(lista_series) == 0:
                print("o estoque está vazio!")
                print('Nenhuma série cadastrada!')
            for serie in lista_series:
                print(serie)
            input('Pressione Enter para continuar...')
        case '3':
            print('Saindo...')
            break
        case _:
            print('Opção inválida!')
            input('Pressione Enter para continuar...')