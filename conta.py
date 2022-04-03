from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta):
        self.__agencia = agencia
        self.__conta = conta
        self._saldo = 0

    @property
    def agencia(self):
        return self.__agencia

    @property
    def conta(self):
        return self.__conta
    
    @property
    def saldo(self):
        return self._saldo
    
    def detalhes(self):
        print()
        print('EXTRATO')
        print(f'Agência: {self.agencia}')
        print(f'Conta: {self.conta}')
        print(f'Saldo em conta R$ {self.saldo:.2f}')
        print()
    
    def depositar(self, value):
        if not isinstance(value, int):
            raise ValueError('É necessário digitar um valor inteiro para ser depositado')
        
        if not value > 0:
            raise ValueError('Para depositar é necessário informar um valor maior que 0.')
        
        self._saldo += value
        print(f'Você depositou R$ {value:.2f}.')
        self.detalhes()
    
    @abstractmethod
    def sacar(self, value): 
        ...

