class Banco(object):
    def __init__(self, taxa_rerserva, total=1000, reserva_exigida=0.1):
        self.__reserva_exigida = reserva_exigida
        self.__total = total
        self.taxa_rerserva = taxa_rerserva
    def __calcula_reserva(self):
        pass
    def pode_fazer_emprestimo(self, valor=None):
        self.valor = bool(valor)

class Conta(object):
    def __init__(self, ID, senha, saldo):
        self.__ID = ID
        self.__senha = senha
        self.__saldo = saldo
    def deposito(self, senha, valor):
        if self.__senha == senha:
            self.__saldo += valor
            print('deposito ok!, saldo: %0.2f' %self.__saldo)
        else:
            print('Senha errada digite novamente...')
    def saque(self, senha, valor):
        if self.__senha == senha:
            if self.__saldo >= valor:
                self.__saldo -= valor
                print('saque ok!, saldo: %0.2f' %self.__saldo)
            else:
                print('Saldo insuficiente!')
        else:
            print('Senha errada digite novamente...')
    def saldo(self):
        print('Saldo: ', self.__saldo)
    
    
        
