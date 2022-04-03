from pessoa_cliente import Pessoa, Cliente
from banco import Banco
from type_contas import ContaCorrente, ContaPoupanca

banco = Banco()


while True:
    name = input("Digite aqui seu nome: ")
    year = int(input("Digite sua idade: "))
    cpf = input("Digite aqui seu CPF (SOMENTE NÚMEROS): ")
    cliente = Cliente(name, year, cpf)

    agencia = int(input("Digite sua agência: "))
    conta = int(input("Digite o número de sua conta: "))
    type_conta = input("Digite 'CC' para conta corrente ou 'CP' para conta poupança: ").upper()
    c = None

    if type_conta == "CC":
        c = ContaCorrente(agencia, conta)
    else:
        c = ContaPoupanca(agencia, conta)
    
    cliente.insere_conta(c)

    banco.inserir_cliente(cliente)
    banco.inserir_conta(c)

    if banco.autentica(cliente):
        while True:
            s_d = input("Digite 'S' para sacar um valor ou 'D' para depositar: ").upper()
            valor = int(input("Digite um valor em R$: "))

            if s_d == "S":
                c.sacar(valor)
                continue
            if s_d == "D":
                c.depositar(valor)
                continue
            else:
                print("Informação não encontrada, tente novamente!")
                continue

    else:
        print("Cliente não autenticado no banco!")
        print("Verifique as informações!")
        break



