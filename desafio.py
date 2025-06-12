from datetime import datetime
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def sacar(valor):
    global saldo, extrato, numero_saques, limite
    if limite < valor:
        print("Valor do saque excede o limite permitido.")
        return False
    elif valor <= 0:
        print("Valor inválido para Saque.")
        return False
    elif valor > saldo:
        print("Saldo insuficiente para saque.")
        return False
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f} - em {datetime.now().date():%d/%m/%Y} às {datetime.now().time():%H:%M:%S}\n"
        if numero_saques == LIMITE_SAQUES:
            print("Número máximo de saques diários excedido.")
            return False
        numero_saques += 1
        return True

def depositar(valor):
    global saldo, extrato
    if valor <= 0:
        print("Valor inválido para depósito.\nDigite um valor positivo.")
        return False
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} - em {datetime.now().date():%d/%m/%Y} às {datetime.now().time():%H:%M:%S}\n"
        return True

def exibir_extrato():
    global extrato, saldo
    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        print('EXTRATO BANCÁRIO'.center(50, "-"))
        for operacao in extrato.split('\n'):
            if operacao.strip():
                print(operacao.center(50, " "))
        print(f"""
    Saldo atual: R$ {saldo:.2f}
    Data: {datetime.now().date():%d/%m/%Y} às {datetime.now().time():%H:%M:%S}
{'-' * 50}
              """)

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))
        if depositar(valor):
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Depósito não realizado.")
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")
            continue
        valor = float(input("Informe o valor do saque: R$ "))
        if sacar(valor):
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saque não realizado.")

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
