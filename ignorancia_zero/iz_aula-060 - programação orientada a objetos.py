class test(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        print('Objeto criado!!')

# alterando e criando atributos fora da classe

test = test()
ok = False

if ok:
    print('Atributo x: ', test.x)
    test.x = 5
    print('Atributo x modificado: ', test.x)
    print('Atributo y: ', test.y)
    test.z = 1
    print('Atributo z criado: ',test.z)

# associações entre objetos

class Pessoa_Animais(object):
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao
    def treinar(self):#esse metodo chama metodos do outro objeto
        self.cao.da_patinha()
        self.cao.latir()

class Cao(object):
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def da_patinha(self):
        print('%s extendeu a patinha' %self.nome)
    def latir(self):
        print('AUAUAUAUAU')

rex = Cao('rex', 'marrom')
jose = Pessoa_Animais('Jose', 75, rex)




