from datetime import datetime
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, cliente, saldo=0.0, limite_saque=500.0, extrato=""):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente # classe Cliente
        self.saldo = saldo
        self.extrato = extrato # classe extrato Historico
        self.data_criacao = datetime.now()
        self.status = True  # Ativo por padrão
    

    def saldo(self):
        return self.saldo
    
    @classmethod
    @abstractmethod
    def nova_conta(cls, agencia, numero, cliente, saldo=0.0, limite_saque=500.0, extrato="", numero_saques=0, limite_saques=3):
        pass
    
    @abstractmethod
    def sacar(self, valor):
        pass
    
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False
        self.saldo += valor
        self.extrato += f"Depósito: R${valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        return True
    
    def transferir(self, valor, conta_destino):
        pass

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, cliente, saldo=0.0, limite_saque=500.0, extrato=None, numero_saques=0, limite_saques=3):
        super().__init__(agencia, numero, cliente, saldo, limite_saque, extrato, numero_saques, limite_saques)
        self.tipo_conta = "Conta Corrente"
        self.numero_saques = numero_saques
        self.limite_saques = limite_saques
    
    def saldo(self):
        return self.saldo
    
    @classmethod
    def nova_conta(self, agencia, numero, cliente, saldo=0.0, limite_saque=500.0, extrato="", numero_saques=0, limite_saques=3):
        return Conta(agencia, numero, cliente, saldo, limite_saque, extrato, numero_saques, limite_saques)
    
    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Número máximo de saques diários excedido.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        if valor > self.limite_saque:
            print("Valor do saque excede o limite.")
            return False
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        self.saldo -= valor
        self.numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
        return True
    
    def transferir(self, valor, conta_destino):
        if self.saldo < valor:
            print("Saldo insuficiente para transferência.")
            return False
        if valor <= 0:
            print("Valor inválido para transferência.")
            return False

        self.saldo -= valor
        conta_destino.saldo += valor
        self.extrato += f"Transferência: R${valor:.2f} para {conta_destino.numero} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        print(f"Transferência de R${valor:.2f} realizada com sucesso.")
        return True

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, cliente, saldo=0, limite_saque=300, extrato="", numero_saques=0, limite_saques=5):
        super().__init__(agencia, numero, cliente, saldo, limite_saque, extrato, numero_saques, limite_saques)
        self.tipo_conta = "Conta Poupança"
        self.numero_saques = numero_saques
        self.limite_saques = limite_saques
    
    def saldo(self):
        return self.saldo
    
    @classmethod
    def nova_conta(self, agencia, numero, cliente, saldo=0.0, limite_saque=500.0, extrato="", numero_saques=0, limite_saques=3):
        return Conta(agencia, numero, cliente, saldo, limite_saque, extrato, numero_saques, limite_saques)
    
    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Número máximo de saques diários excedido.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        if valor > self.limite_saque:
            print("Valor do saque excede o limite.")
            return False
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        self.saldo -= valor
        self.numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
        return True
    
    def transferir(self, valor, conta_destino):
        if self.saldo < valor:
            print("Saldo insuficiente para transferência.")
            return False
        if valor <= 0:
            print("Valor inválido para transferência.")
            return False

        self.saldo -= valor
        conta_destino.saldo += valor
        self.extrato += f"Transferência: R${valor:.2f} para {conta_destino.numero} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        print(f"Transferência de R${valor:.2f} realizada com sucesso.")
        return True

class Transaction(ABC): #classe abstrata interface
    @abstractmethod
    def realizar_transacao(self, conta):
        pass

class Depositar(Transaction):
    def __init__(self, valor):
        self.valor = valor

    def realizar_transacao(self, conta):
        conta.saldo += self.valor
        print(f"Depósito de R${self.valor:.2f} realizado com sucesso.")

class Sacar(Transaction):
    def __init__(self, valor):
        self.valor = valor

    def realizar_transacao(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            print(f"Saque de R${self.valor:.2f} realizado com sucesso.")
            return True
        else:
            print("Saldo insuficiente.")
            return False

class Transferir(Transaction):
    def __init__(self, valor, conta_destino):
        self.valor = valor
        self.conta_destino = conta_destino

    def realizar_transacao(self, conta_origem):
        if conta_origem.saldo >= self.valor:
            conta_origem.saldo -= self.valor
            self.conta_destino.saldo += self.valor
            print(f"Transferência de R${self.valor:.2f} realizada com sucesso.")
        else:
            print("Saldo insuficiente para transferência.")

