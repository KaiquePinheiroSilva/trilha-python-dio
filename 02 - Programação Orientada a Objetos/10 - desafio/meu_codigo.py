import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime 

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero_conta, agencia):
        self._saldo = 0
        self._numero_conta = numero_conta
        self._agencia = agencia
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero_conta):
        return cls(cliente, numero_conta)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("transação falhou, valor de saque excedeu o saldo") 
            return False
        elif valor > 0:
            saldo -= valor
            print(f"transação sucedida, novo valor em conta: R$ {saldo}")
            return True
        return False

    def depositar(self, valor):
        saldo = self.saldo

        if valor <= 0:
            print("transação falhou, valor inválido")
            return False
        else:
            saldo += valor
            print(f"transação sucedida, novo valor em conta: R$ {saldo}")
            return True

class ContaCorrente(Conta):
    def __init__(self, numero_conta, agencia):
        super().__init__(numero_conta, agencia)
        self._limite = 500
        self._limite_saques = 3

class Transacao(ABC):

    @abstractclassmethod
    def registrar(self, conta):
        pass
    
    @property
    @abstractproperty
    def valor(self):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)
    
class Saque(Deposito):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


