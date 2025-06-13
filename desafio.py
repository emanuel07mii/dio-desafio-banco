from datetime import datetime

def selecionar_opcao(opcao):
    if opcao == "d":
        return "Depositar"
    elif opcao == "s":
        return "Sacar"
    elif opcao == "e":
        return "Extrato"
    elif opcao == "u":
        return "Criar Usuário"
    elif opcao == "c":
        return "Criar Conta Corrente"
    elif opcao == "l":
        return "Listar Contas"
    elif opcao == "lu":
        return "Listar Usuários"
    elif opcao == "q":
        return "Sair"
    else:
        return "Operação inválida, por favor selecione novamente a operação desejada."


def menu_principal():
    menu = (
    "[d] Depositar\n[s] Sacar\n[e] Extrato\n"
    "[u] Criar Usuário\n[c] Criar Conta corrente\n"
    "[l] Listar Contas\n[lu] Listar Usuários\n[q] Sair"
    )
    print("\nBem-vindo ao Sistema Bancário!")
    print("Selecione uma das opções abaixo:")
    print(menu)
    op = str(input("=> ").strip().lower())
    return selecionar_opcao(op)

def criar_usuario(usuarios, cpf, nome, data_nascimento, endereco):
    if any(u['cpf'] == cpf for u in usuarios):
        print("Usuário já existe.")
        return usuarios
    usuario = {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": datetime.strptime(data_nascimento, "%d/%m/%Y").date(),
        "endereco": endereco
    }
    usuarios.append(usuario)
    return usuarios

def encontrar_usuario(usuarios, cpf):
    return next((u for u in usuarios if u["cpf"] == cpf), None)

def criar_conta(contas, usuarios, cpf):
    usuario = encontrar_usuario(usuarios, cpf)
    if not usuario:
        print("Usuário não encontrado.")
        return contas
    numero = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero": str(numero),
        "cliente": usuario,
        "saldo": 0.0,
        "limite_saque": 500.0,
        "extrato": "",
        "numero_saques": 0,
        "limite_saques": 3,
        "data_criacao": datetime.now(),
        "data_atualizacao": datetime.now(),
        "status": True,
        "tipo_conta": "Conta Corrente",
        "tipo_usuario": "Cliente"
    }
    contas.append(conta)
    return contas

def encontrar_conta(contas, cpf):
    return next((c for c in contas if c["cliente"]["cpf"] == cpf), None)

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Número máximo de saques diários excedido.")
        return saldo, extrato, numero_saques, False
    if valor > saldo:
        print("Saldo insuficiente.")
        return saldo, extrato, numero_saques, False
    if valor > limite:
        print("Valor do saque excede o limite.")
        return saldo, extrato, numero_saques, False
    if valor <= 0:
        print("Valor inválido para saque.")
        return saldo, extrato, numero_saques, False

    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
    numero_saques += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato, numero_saques, True

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Valor inválido para depósito.")
        return saldo, extrato, False
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato, True

def exibir_extrato(saldo, /, *, extrato):
    print(extrato if extrato else "Nenhuma transação realizada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print('-' * 50)

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\nLISTAGEM DE CONTAS".center(50, "-"))
    for conta in contas:
        cliente = conta["cliente"]
        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"Conta: Agência {conta['agencia']} - Número {conta['numero']}")
        print("-" * 50)

def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print("\nLISTAGEM DE USUÁRIOS".center(50, "-"))
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Nascimento: {usuario['data_nascimento'].strftime('%d/%m/%Y')}")
        print(f"Endereço: {usuario['endereco']}")
        print("-" * 50)


def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu_principal()

        if opcao == "Criar Usuário":
            cpf = input("Informe o CPF (somente números): ").strip()
            nome = input("Nome completo: ").strip()
            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
            endereco = input("Endereço (Rua, Número - Bairro - Cidade/UF): ").strip()
            usuarios = criar_usuario(usuarios, cpf, nome, data_nascimento, endereco)
            print("Usuário criado com sucesso!")

        elif opcao == "Criar Conta Corrente":
            cpf = input("Informe o CPF do titular: ").strip()
            contas = criar_conta(contas, usuarios, cpf)
            print("Conta corrente criada com sucesso!")

        elif opcao == "Depositar":
            cpf = input("Informe o CPF do titular: ").strip()
            conta = encontrar_conta(contas, cpf)
            if conta:
                valor = float(input("Informe o valor do depósito: R$ "))
                conta["saldo"], conta["extrato"], _ = depositar(conta["saldo"], valor, conta["extrato"])
            else:
                print("Conta não encontrada.")

        elif opcao == "Sacar":
            cpf = input("Informe o CPF do titular: ").strip()
            conta = encontrar_conta(contas, cpf)
            if conta:
                valor = float(input("Informe o valor do saque: R$ "))
                conta["saldo"], conta["extrato"], conta["numero_saques"], _ = sacar(
                    saldo=conta["saldo"],
                    valor=valor,
                    extrato=conta["extrato"],
                    limite=conta["limite_saque"],
                    numero_saques=conta["numero_saques"],
                    limite_saques=conta["limite_saques"]
                )
            else:
                print("Conta não encontrada.")

        elif opcao == "Extrato":
            cpf = input("Informe o CPF do titular: ").strip()
            conta = encontrar_conta(contas, cpf)
            if conta:
                print('EXTRATO BANCÁRIO'.center(50, "-"))
                print(f"Conta {conta['numero']} - Agência {conta['agencia']} - Tipo: {conta['tipo_conta']}")
                print(f"Titular: {conta['cliente']['nome']} - CPF: {conta['cliente']['cpf']}")
                print("-" * 50)
                exibir_extrato(conta["saldo"], extrato=conta["extrato"])
            else:
                print("Conta não encontrada.")
        
        elif opcao == "Listar Contas":
            listar_contas(contas)
        
        elif opcao == "Listar Usuários":
            listar_usuarios(usuarios)

        elif opcao == "Sair":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print(opcao)

if __name__ == "__main__":
    main()
