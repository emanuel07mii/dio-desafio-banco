# 🔍 Desafio prático
Criando um sistema bancário com Python

## 🏦 Objetivo
Nessa primeira etapa temos que criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

### ⚙️💵 1.Operação de depósito
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.


### ⚙️💵 2.Operação de saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### ⚙️💵 3.Operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para clonar e executar o projeto localmente:

### 1. Clone o repositório

```bash
git clone git@github.com:emanuel07mii/dio-desafio-banco.git
```
- Acesse a pasta raiz do projeto
```bash
cd dio-desafio-banco
```
### 2. Execute o código desafio.py
```bash
python desafio.py
```
ou
```bash
python3 desafio.py
```

## 📚 Referências

1. Repositório com toda a [trilha python da Dio.](https://github.com/digitalinnovationone/trilha-python-dio)
2. Código da aula de [resolução do desafio.](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py)
