class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print('CC Nº %s  Saldo: %0.2f' %(self.numero, self.saldo))
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque', valor])
        else:
            print('Saldo insuficiente!')
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['Depósito', valor])
    def extrato(self):
        print('Extrato CC Nº %s' %(self.numero))
        for op in self.operacoes:
            print('%10s %10.2f' %(op[0], op[1]))
        print('%10s %10.2f\n' %('saldo=', self.saldo))

