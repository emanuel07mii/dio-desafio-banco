from datetime import datetime
from abc import ABC, abstractmethod

class Transacao(ABC): #classe abstrata interface

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    def registrar(self, conta):
        return conta.depositar(self.valor)

    # def realizar_transacao(self, conta):
    #     if conta.depositar(self.valor):
    #         transacao = f"Depósito: R${self.valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    #         self.registrar(transacao)

    #     conta.saldo += self.valor
    #     print(f"Depósito de R${self.valor:.2f} realizado com sucesso.")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    def registrar(self, conta):
        return conta.sacar(self.valor)

    # def realizar_transacao(self, conta):
    #     if conta.saldo >= self.valor:
    #         conta.saldo -= self.valor
    #         print(f"Saque de R${self.valor:.2f} realizado com sucesso.")
    #         return True
    #     else:
    #         print("Saldo insuficiente.")
    #         return False

class Transferir(Transacao):
    def __init__(self, valor, conta_destino):
        self.valor = valor
        self.conta_destino = conta_destino
    
    def resistrar(self, conta_origem):
        return conta_origem.transferir(self.valor, self.conta_destino)

    # def realizar_transacao(self, conta_origem):
    #     if conta_origem.saldo >= self.valor:
    #         conta_origem.saldo -= self.valor
    #         self.conta_destino.saldo += self.valor
    #         print(f"Transferência de R${self.valor:.2f} realizada com sucesso.")
    #     else:
    #         print("Saldo insuficiente para transferência.")

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
    
    def exibir_extrato(self):
        if not self.transacoes:
            print("Nenhuma transação realizada.")
            return
        print("Extrato - Histórico de Transações")
        print('-' * 60)
        for transacao in self.transacoes:
            print(transacao)
        print('-' * 60)
        print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

class Conta(ABC):
    def __init__(self, agencia, numero, cliente, saldo=0.0, limite_saque=500.0, extrato=None, numero_saques=0, limite_saques=0, tipo_conta="Conta Corrente"):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente # classe Cliente
        self.saldo = saldo
        self.extrato = Historico() # classe extrato Historico
        self.data_criacao = datetime.now()
        self.status = True  # Ativo por padrão
    
    @classmethod
    @abstractmethod
    def nova_conta(cls, agencia, numero, cliente, saldo=0.0, extrato=""):
        return Conta(agencia, numero, cliente, saldo, extrato)
    
    @abstractmethod
    def sacar(self, valor):
        pass
    
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False
        self.saldo += valor
        self.extrato.adicionar_transacao(f"Depósito: R${valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        return True
    
    def transferir(self, valor, conta_destino):
        pass

    def exibir_extrato(self):
        self.extrato.exibir_extrato()
        print(f"Titular: {self.cliente.nome} Nº{self.tipo_conta}: {self.numero} AG: {self.agencia}")
        print(f"Saldo atual: R${self.saldo:.2f} L de saque: R${self.limite_saque:.2f} Nº Saques: {self.numero_saques}")
        print(60 * "-")

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, cliente, saldo=0.0, limite_saque=500.0, extrato=None, numero_saques=0, limite_saques=5):
        super().__init__(agencia, numero, cliente, saldo, limite_saque, extrato, numero_saques, limite_saques)
        self.tipo_conta = "Conta Corrente"
        self.numero_saques = numero_saques
        self.limite_saques = limite_saques
        self.limite_saque = limite_saque
    
    def saldo(self):
        return self.saldo
    
    @classmethod
    def nova_conta(cls, agencia, numero, cliente, saldo=0.0, limite_saque=500.0, extrato="", numero_saques=0, limite_saques=5, tipo_conta="Conta Corrente"):
        return Conta(agencia, numero, cliente, saldo, limite_saque, extrato, numero_saques, limite_saques, tipo_conta)
    
    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques or valor > self.saldo or valor > self.limite_saque or valor <= 0:
            print("Saque não realizado. Verifique o valor, número de saques e tente novamente.")
            return False

        self.saldo -= valor
        self.numero_saques += 1
        self.extrato.adicionar_transacao(f"Saque: R${valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
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
        self.extrato.append(f"Transferência: R${valor:.2f} para {conta_destino.numero} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        print(f"Transferência de R${valor:.2f} realizada com sucesso.")
        return True

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, cliente, saldo=0, limite_saque=300, extrato="", numero_saques=0, limite_saques=3):
        super().__init__(agencia, numero, cliente, saldo, limite_saque, extrato, numero_saques, limite_saques)
        self.tipo_conta = "Conta Poupança"
        self.numero_saques = numero_saques
        self.limite_saques = limite_saques
        self.limite_saque = limite_saque
    
    def saldo(self):
        return self.saldo
    
    @classmethod
    def nova_conta(cls, agencia, numero, cliente, saldo=0.0, limite_saque=300.0, extrato="", numero_saques=0, limite_saques=3, tipo_conta="Conta Poupança"):
        return Conta(agencia, numero, cliente, saldo, limite_saque, extrato, numero_saques, limite_saques, tipo_conta)
    
    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques or valor > self.saldo or valor > self.limite_saque or valor <= 0:
            print("Número máximo de saques diários excedido ou valor invalido, verifique e tente Novamente.")
            return False

        self.saldo -= valor
        self.numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
        self.extrato.adicionar_transacao(f"Saque: R${valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        return True
    
    def transferir(self, valor, conta_destino):
        if self.saldo < valor:
            print("Saldo insuficiente para transferência.")
            return False
        if valor <= 0:
            print("Valor inválido para transferência.")
            return False
        
        if self.sacar(valor):
            conta_destino.depositar(valor)
            self.extrato.adicionar_transacao(f"Transferência: R${valor:.2f} para {conta_destino.numero} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Transferência de R${valor:.2f} realizada com sucesso para {conta_destino.nome}.")
            return True

        self.saldo -= valor
        conta_destino.saldo += valor
        self.extrato.append(f"Transferência: R${valor:.2f} para {conta_destino.numero} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        print(f"Transferência de R${valor:.2f} realizada com sucesso.")
        return True
