# abstração criar metodos na super classe

class Objeto_grafico(object):
    def __init__(self, cor):
        self.cor = cor
    def area(self): #metodos abstratos vao ter que ser preenchidos na subclasse
        pass
    def perimetro(self): #metodos abstratos
        pass
    def info(self):
        print('%f metro2 serão preenchidos com a cor %s' %(self.area(), self.cor))


class Cao(object):
    nome = 'Rex' # atributos estáticos da classe Cao podem ser 
    cor = 'Marrom' # acessados de qualquer instancia da classe

class Conta(object):
    __total = 10000  # atributo privado e estático
    reserva = 0.1 # atributo estáticos
    def __init__(self, ID, saldo=0):
        self.__ID = ID # __ID (os dois "_" deixam o atributo privado)
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
        Conta.__total += valor
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            Conta.__total -= valor
        else:
            print('Saldo insuficiente: %0.2f' %self.saldo)
        Conta.__imprime_reserva()
    def __imprime_reserva(): # Metodo estático so imprime se chamar de dentro da classe
        print(Conta.__total * Conta.reserva)
            
