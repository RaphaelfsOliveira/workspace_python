import pickle

arq = open('arquivo.pck', 'wb')
l1 = [1, 2, 3]
pickle.dump(l1, arq)

print(pickle.dumps(l1))

class Pessoa:
    def __init__(self, n, p):
        self.n = n
        self.p = p
    def ola(self):
        print('Ola sou %s e peso %s' %(self.n, self.p))

pedro = Pessoa('Pedro', 75)

# com pickle voce pode escrever objetos criados em arquivos
pickle.dump(pedro, arq)
arq.close()

arq = open('arquivo.pck', 'rb')
x = pickle.load(arq)
y = pickle.load(arq)

print(x)
print(y, y.__dict__)



