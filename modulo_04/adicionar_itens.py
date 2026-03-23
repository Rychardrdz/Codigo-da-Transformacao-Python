'''
Atividade 1
'''

lista_compras = []

# Loop principal do programa
while True:
    print("\n--- Lista de Compras ---")
    print("1 - Adicionar item")
    print("2 - Ver lista")
    print("3 - Remover item")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o nome do item que deseja adicionar: ")
        lista_compras.append(item)
        print(f'"{item}" foi adicionado à lista.')

    elif opcao == "2":
        print("\nSua lista de compras:")
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")

    elif opcao == "3":
        item = input("Digite o nome do item que deseja remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f'"{item}" foi removido da lista.')
        else:
            print("Esse item não está na lista.")

    elif opcao == "0":
        print("Encerrando a lista de compras.")
        break

    else:
        print("Opção inválida. Tente novamente.")