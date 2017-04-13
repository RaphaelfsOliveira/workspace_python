import math

class Objeto_grafico(object):
    def __init__(self, cor_pre, pre, cor_con):
        self.cor_preenchimento = cor_pre
        self.cor_contorno = cor_con
        self.preenchida = bool(pre)

class Retangulo(Objeto_grafico):
    def __init__(self, b, a, cor_pre, pre, cor_con):
        super(Retangulo, self).__init__(cor_pre, pre, cor_con)
        self.base = b
        self.altura = a
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return (self.base + self.altura) * 2

class Circulo(Objeto_grafico):
    def __init__(self, raio, cor_pre, pre, cor_con):
        super(Circulo, self).__init__(cor_pre, pre, cor_con)
        self.r = raio
    def area(self):
        return math.pi * self.r**2
    def diametro(self):
        return self.r * 2

class Quadrado(Objeto_grafico):
    def __init__(self, lado, cor_pre, pre, cor_con):
        super(Quadrado, self).__init__(cor_pre, pre, cor_con)
        self.lado = lado
    def area(self):
        return self.lado**2
    def perimetro(self):
        return self.lado * 4


        
        
        
        
