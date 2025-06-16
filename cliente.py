from datetime import datetime
from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, cpf, nome, data_nascimento, endereco, coontas=None):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        self.endereco = endereco
        self.contas = coontas if coontas is not None else []
    
    @abstractmethod
    def realizar_transacao(self, transacao):
        pass

    @abstractmethod
    def adicionar_conta(self, conta):
        pass

    def cliente_dados(self):
        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento.strftime("%d/%m/%Y"),
            "endereco": self.endereco,
            "tipo_usuario": self.tipo_usuario
        }

# função para criar conta

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, coontas=None):
        super().__init__(cpf, nome, data_nascimento, endereco, coontas)
        self.tipo_usuario = "Pessoa Física"
    
    def realizar_transacao(self, transacao):
        return super().realizar_transacao(transacao)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"Conta {conta.numero} adicionada com sucesso para {self.nome}.")

class PessoaJuridica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, coontas=None):
        super().__init__(cpf, nome, data_nascimento, endereco, coontas)
        self.tipo_usuario = "Pessoa Jurídica"
    
    def realizar_transacao(self, transacao):
        return super().realizar_transacao(transacao)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"Conta {conta.numero} adicionada com sucesso para {self.nome}.")

    def cliente_dados(self):
        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento.strftime("%d/%m/%Y"),
            "endereco": self.endereco,
            "tipo_usuario": self.tipo_usuario
        }
