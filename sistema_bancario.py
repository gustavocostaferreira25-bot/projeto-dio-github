saldo = 0

while True:
    print("\n=== Banco DIO ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Valor do depósito: "))
        saldo += valor
        print("Depósito realizado com sucesso!")

    elif opcao == "2":
        valor = float(input("Valor do saque: "))
        if valor <= saldo:
            saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

    elif opcao == "3":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")
