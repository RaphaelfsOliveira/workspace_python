class quadrado(object):
    def __init__(self, l):
        self.lado = l

    def m_lado(self, l):
        self.lado = l

    def v_lado(self):
        return self.lado

    def area(self):
        return self.lado * self.lado


class retangulo(object):
    def __init__(self, a, b):
        self.base = b
        self.altura = a

    def muda_lados(self, a, b):
        self.base = b
        self.altura = a

    def lados(self):
        return self.base, self.altura

    def area(self):
        return self.base * self.altura

    def perim(self):
        return (self.base + self.altura) * 2



def comodo():
    print('digite abaixo a medida do comodo que precisa dos pisos:')
    a = float(input('Comprimento.: '))
    b = float(input('Largura.: '))
    c = retangulo(a, b)
    return round(c.area(), 2)

def piso():
    l = float(input('Digite o lado do piso.: '))
    p = quadrado(l)
    return round(p.area(), 2)

def quant_pisos(comodo, piso):
    return (comodo / piso) * 1.1

###Classe Pessoa

class pessoa(object):
    def __init__(self, n, i, p, a):
        self.nome = n
        self.idade = i
        self.peso = p
        self.altura = a

    def envelhecer(self, i=1):
        if self.idade < 21:
            self.altura += (i * 0.05)
        self.idade += i

    def engordar(self, p):
        self.peso += p

    def emagrecer(self, p):
        self.peso -= p

    def crescer(self, a):
        self.altura += a
        

if __name__ == '__main__':

    #print(quant_pisos(comodo(), piso()))

    pass    
        
