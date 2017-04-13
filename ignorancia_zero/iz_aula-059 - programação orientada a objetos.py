# Objetos Sintaxe

class my_object(object):
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        print('construtor chamado com sucesso!')

    def printer(self, x, *args):
        print('Ola meu nome é %s e eu tenho %d anos' %(self.name, self.age))
        return x * x


class quadrado(object):
    def __init__(self, l):
        self.lado = l

    def m_lado(self, l):
        self.lado = l

    def v_lado(self):
        return self.lado

    def area(self):
        return self.lado * self.lado
