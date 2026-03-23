'''
Desafio Extra
'''

agenda = {}

while True:
    print("\n--- Agenda de Contatos ---")
    print("1 - Adicionar contato")
    print("2 - Ver contatos")
    print("3 - Buscar Contatos")
    print("4 - Remover contato")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        print("Contato adicionado com sucesso.")

    elif opcao == "2":
        if agenda:
            print("Contatos na agenda:")
            for nome, telefone in agenda.items():
                print(f"{nome} - {telefone}")
        else:
            print("A agenda está vazia.")

    elif opcao == "3":
        nome = input("Digite o nome do contato a ser buscado: ")
        if nome in agenda:
            print(f"Contato encontrado: {nome} - {agenda[nome]}")
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        nome = input("Digite o nome do contato a ser removido: ")
        if nome in agenda:
            del agenda[nome]
            print("Contato removido com sucesso.")
        else:
            print("Contato não encontrado.")

    elif opcao == "0":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")