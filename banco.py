class Banco:
    def __init__(self):
        self.agencias = [2565, 2789, 3014]
        self.contas = []
        self.clientes = []
    
    def inserir_conta(self, conta):
        self.contas.append(conta)
    
    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def autentica(self, cliente):
        if cliente not in self.clientes:
            return False
        
        if cliente.conta not in self.contas:
            return False
        
        if cliente.conta.agencia not in self.agencias:
            print(f'Agência {cliente.conta.agencia} não existe em nosso banco.')
            return False
        
        if not cliente._valida_cpf():
            return False
        
        return True

