class Pessoa:
    def __init__(self, nome, idade, cpf):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def cpf(self):
        return self._cpf

    @property
    def cpf_valido(self):
        return self._cpf_valido
    
    @staticmethod
    def formata(cpf):
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    
    def _valida_cpf(self):
        novo_cpf = self.cpf[:9]
        total = 0
        reverso = 10

        for index in range(19):
            if index > 8:
                index -= 9
            
            total += int(novo_cpf[index]) * reverso

            reverso -= 1
            if reverso < 2:
                reverso = 11
                digito = 11 - (total % 11)

                if digito > 9:
                    digito = 0
                
                total = 0
                novo_cpf += str(digito)
        
        if not novo_cpf == self.cpf:
            return False
        else:
            return True
    

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)
        self._conta = None
    
    @property
    def conta(self):
        return self._conta
    
    def insere_conta(self, conta):
        self._conta = conta

