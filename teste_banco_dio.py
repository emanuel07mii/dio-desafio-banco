import time
from banco_teste import criar_cliente, criar_conta, depositar, sacar, exibir_extrato, salvar_dados_csv, carregar_dados_csv

def simular_uso_banco():
    # Carrega dados (ou inicia vazios se arquivos não existem)
    clientes, contas = carregar_dados_csv()

    print("\n--- Criando clientes ---")
    # Simula entrada de dois clientes
    inputs_cliente = iter([
        "11111111111", "João Silva", "01-01-1990", "Rua A, 123 - Centro - Cidade/UF",
        "22222222222", "Maria Souza", "02-02-1992", "Rua B, 456 - Bairro - Cidade/UF",
    ])

    input_backup = __builtins__.input
    __builtins__.input = lambda _: next(inputs_cliente)
    criar_cliente(clientes)
    time.sleep(2)
    criar_cliente(clientes)
    __builtins__.input = input_backup
    salvar_dados_csv(clientes, contas)

    print("\n--- Criando contas ---")
    inputs_conta = iter(["11111111111", "22222222222"])
    __builtins__.input = lambda _: next(inputs_conta)
    criar_conta(1, clientes, contas)
    time.sleep(2)
    criar_conta(2, clientes, contas)
    __builtins__.input = input_backup
    salvar_dados_csv(clientes, contas)

    print("\n--- Realizando depósitos ---")
    inputs_deposito = iter(["11111111111", "1000", "22222222222", "500"])
    __builtins__.input = lambda _: next(inputs_deposito)
    depositar(clientes)
    time.sleep(2)
    depositar(clientes)
    __builtins__.input = input_backup
    salvar_dados_csv(clientes, contas)

    print("\n--- Realizando saques válidos ---")
    inputs_saque_validos = iter(["11111111111", "200", "11111111111", "300"])
    __builtins__.input = lambda _: next(inputs_saque_validos)
    sacar(clientes)
    time.sleep(2)
    sacar(clientes)
    __builtins__.input = input_backup
    salvar_dados_csv(clientes, contas)

    print("\n--- Tentando saque inválido (excesso diário) ---")
    inputs_saque_invalido = iter(["11111111111", "100"])
    __builtins__.input = lambda _: next(inputs_saque_invalido)
    sacar(clientes)  # Terceiro saque no mesmo dia deve falhar
    __builtins__.input = input_backup
    time.sleep(2)

    print("\n--- Exibindo extratos ---")
    inputs_extrato = iter(["11111111111", "22222222222"])
    __builtins__.input = lambda _: next(inputs_extrato)
    exibir_extrato(clientes)
    time.sleep(2)
    exibir_extrato(clientes)
    __builtins__.input = input_backup

    salvar_dados_csv(clientes, contas)
    print("\n--- Teste finalizado com sucesso ---")

if __name__ == "__main__":
    simular_uso_banco()
