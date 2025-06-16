from datetime import datetime

class Cliente:
    def __init__(self, cpf, nome, data_nascimento, endereco, coontas=None):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        self.endereco = endereco
        self.contas = coontas if coontas is not None else []

# função para criar conta

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, coontas=None):
        super().__init__(cpf, nome, data_nascimento, endereco, coontas)
        self.tipo_usuario = "Pessoa Física" 

class PessoaJuridica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, coontas=None):
        super().__init__(cpf, nome, data_nascimento, endereco, coontas)
        self.tipo_usuario = "Pessoa Jurídica"
