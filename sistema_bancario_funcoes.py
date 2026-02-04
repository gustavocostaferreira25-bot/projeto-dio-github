def depositar(saldo):
    valor = float(input("Valor do depósito: "))
    if valor > 0:
        saldo += valor
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")
    return saldo


def sacar(saldo):
    valor = float(input("Valor do saque: "))
    if valor <= saldo:
        saldo -= valor
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente.")
    return saldo


def ver_saldo(saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")


def menu():
    print("\n=== Banco DIO ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("0 - Sair")
    return input("Escolha uma opção: ")


saldo = 0

while True:
    opcao = menu()

    if opcao == "1":
        saldo = depositar(saldo)

    elif opcao == "2":
        saldo = sacar(saldo)

    elif opcao == "3":
        ver_saldo(saldo)

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")
