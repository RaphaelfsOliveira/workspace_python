## statement Del e is

x = 10

print(x)

del x  #deleta o x

l = [1, 2, 3]

del l[1]

print(l)

d = {'a': 1, 'b': 2, 'c': 3}

del d['b']

print(d)


class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresenta(self):
        print('Ola meu nome é %s' %self.nome)


joao = Pessoa('Joao', 23)


# comparação IS

l = [1,2,3]
l2 = l
l is l2




