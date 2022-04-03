from conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, value):
        if self.saldo < value:
            print('Saldo insuficiente!')
            return

        if not isinstance(value, int):
            raise ValueError('É necessário informar um valor inteiro para saca-lo!')
        
        if value < 15:
            print('Não é possível sacar um valor abaixo de R$ 15.00')
            return
        
        self._saldo -= value
        print(f'Você sacou R$ {value:.2f}')
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta):
        super().__init__(agencia, conta)
        self._limite = 200
    
    @property
    def limite(self):
        return self._limite
    
    def sacar(self, value):
        if not isinstance(value, int):
            raise ValueError(f'É necessário informar um valor inteiro para saca-lo!')
        
        if (self.limite + self.saldo) < value:
            print(f'Saldo insuficiente! Saldo disponível para saque (Limite + Saldo em conta) R$ {self.limite + self.saldo:.2f}')
            return
        
        if value < 50:
            print('Não é possível sacar um valor abaixo de R$ 50.00.')
            return
        
        self._saldo -= value
        print(f'Você sacaou {value:.2f}')
        self.detalhes()

