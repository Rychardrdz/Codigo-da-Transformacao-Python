'''
Atividade 3
'''

while True:
    print("\n--- MENU ---")
    print("1 - Verificar se o número é par ou ímpar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = int(input("Digite um número inteiro: "))
        
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")

    elif opcao == "0":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")