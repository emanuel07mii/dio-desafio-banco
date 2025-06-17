from cliente import PessoaFisica, PessoaJuridica
from banco import Conta, ContaCorrente, ContaPoupanca, Historico, Deposito, Saque
import time

c2 = PessoaFisica("98765432100", "Maria Oliveira", "15/05/1985", "Rua B, 456")
# print(f"Cliente criado: {c2.nome}, CPF: {c2.cpf}, Data de Nascimento: {c2.data_nascimento}, Endereço: {c2.endereco}")
c3 = PessoaJuridica("12345678000195", "Empresa XYZ", "20/10/2000", "Avenida C, 789")
# print(f"Cliente criado: {c3.nome}, CNPJ: {c3.cpf}, Data de Fundação: {c3.data_nascimento}, Endereço: {c3.endereco}")

# print("\nTestando Metodo de Cliente")
# print("Cliente 2", c2.cliente_dados())
# print("Cliente 3", c3.cliente_dados())

print("\nTestando Contas / Banco")

cc = ContaCorrente(
    agencia="001",
    numero="12345-6",
    cliente=c2,
    saldo=0,
    limite_saque=500.0,
    extrato=Historico(),
    numero_saques=0,
    limite_saques=5,
)

cp = ContaPoupanca(
    agencia="001",
    numero="65432-1",
    cliente=c3,
    saldo=0,
    limite_saque=300.0,
    extrato=Historico(),
    numero_saques=0,
    limite_saques=3,
)

print(f"Conta Corrente criada: {cc.numero} - Agência {cc.agencia} - Cliente: {cc.cliente.nome}")
print(f"Conta Poupança criada: {cp.numero} - Agência {cp.agencia} - Cliente: {cp.cliente.nome}\n")

print("Testando Saque e Depósito - Conta Corrente")

deposito = Deposito(200.0)
deposito.registrar(cc)
time.sleep(2)

saque = Saque(25.0)
saque.registrar(cc)
time.sleep(2)

saque = Saque(30.0)
saque.registrar(cc)
time.sleep(2)

deposito = Deposito(100.0)
deposito.registrar(cc)
time.sleep(2)

saque = Saque(15.0)
saque.registrar(cc)
time.sleep(2)

saque = Saque(5.0)
saque.registrar(cc)
time.sleep(2)

saque = Saque(45.0)
saque.registrar(cc)
time.sleep(2)

print(50*"-", "\n")
# ---------------------------------------------------------------
print("Testando Saque e Depósito - Conta Poupança")
depositocp = Deposito(150.0)
depositocp.registrar(cp)
time.sleep(2)

saquecp = Saque(10.0)
saquecp.registrar(cp)
time.sleep(2)

depositocp = Deposito(100.0)
depositocp.registrar(cp)
time.sleep(2)

saquecp = Saque(20.0)
saquecp.registrar(cp)
time.sleep(2)

saquecp = Saque(70.0)
saquecp.registrar(cp)
time.sleep(2)

print("\n", 50*"-", "\n")
print(f"Saldo Conta Corrente c2: R$ {cc.saldo:.2f}")
print(f"Saldo Conta Poupança c3: R$ {cp.saldo:.2f}\n")
print(60*"-", "\n")
cc.exibir_extrato()
print("\n")
cp.exibir_extrato()

print("\n", 50*"-")
print("Testando Saque e Depósito - Com erros")

deposito = Deposito(-200.0) # Erro deposito de valor negaivo
deposito.registrar(cc)
time.sleep(2)

print("Tentativa de saque (Valor limite de saque) - Conta corrente")
saque = Saque(600.0) # Erro valor limite de saque
saque.registrar(cc)
time.sleep(2)

depositocp = Deposito(-150.0) # Erro deposito de valor negaivo
depositocp.registrar(cp)
time.sleep(2)

print("Tentativa de saque (Valor limite de saque) - Conta Poupança")
saquecp = Saque(301.0) # Erro valor limite de saque
saquecp.registrar(cp)

print(50*"-", "\n\n")
print(f"Saldo Conta Corrente c2: R$ {cc.saldo:.2f}")
print(f"Saldo Conta Poupança c3: R$ {cp.saldo:.2f}\n")
print(60*"-", "\n")
cc.exibir_extrato()
print("\n")
cp.exibir_extrato()