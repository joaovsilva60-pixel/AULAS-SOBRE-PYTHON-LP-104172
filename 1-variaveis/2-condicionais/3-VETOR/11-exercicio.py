import os

lista_produtos = []

while True:
    os.system("cls")

    print('''
===MERCADO DENDEIZEIROS ===
1-  CADASTRAR PRODUTO
2-  LISTAR PRODUTOS
3-  sAIR
    ''''')
    opcao = input('Escolha uma opção: ')
    match opcao:
        case '1':
            
            nome = input('Digite o nome do produto: ').strip().upper()

            lista_produtos.append(nome)
            print(f'Produto  cadastrado com sucesso!')
            input('Pressione Enter para continuar...')
        case '2':
            print('=== LISTAR PRODUTOS ===')
            if len(lista_produtos) == 0:
                print("o estoque está vazio!")
                print('Nenhum produto cadastrado!')
            for produto in lista_produtos:
                print(produto)
            input('Pressione Enter para continuar...')
        case '3':
            print('Saindo...')
            break
        case _:
            print('Opção inválida!')
            input('Pressione Enter para continuar...')