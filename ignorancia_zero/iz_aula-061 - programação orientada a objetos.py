
Pessoa = {'Nome': 'Lucas',
          'Emprego': 'Advogado',
          'Idade': 20,
          'Cor do Cabelo': 'Preto'}

class Pessoa(object):
    def __init__(self, nome, emprego, idade):
        self.nome = nome
        self.emprego = emprego
        self.idade = idade
    def ola(self):
        print('Ola meu nome é %s tenho %d anos e sou %s' %(self.nome, self.idade, \
                                                           self.emprego))
                                                           


lucas = Pessoa('Lucas', 'Engenheiro', 27)
print(lucas.__dict__) #objetos são armazenados em dicionarios isso torna o python mais lento
print()
print(Pessoa.__dict__)
