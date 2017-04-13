class Mamifero(object):
    def __init__(self, cor_pelo, genero, num_patas):
        self.cor_pelo = cor_pelo
        self.genero = genero
        self.num_patas = num_patas
    def falar(self):
        print('Ola eu sou um mamifero e sei falar!')
    def andar(self):
        print('Estou andando sobre %d patas' %self.num_patas)
    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print('%s não amamenta' %self.genero)
            return
        print('Amamentando meu filhote..')


# super chama todos os atributos ou metodos da superclasse
# para quando precisar reescrever os atributos ou metodos

class Pessoa(Mamifero):
    def __init__(self, cor_pelo, genero, num_patas, cabelo):
        super(Pessoa, self).__init__(cor_pelo, genero, num_patas) 
        self.cabelo = cabelo
    def falar(self):
        super(Pessoa, self).falar()
        print('Ola eu sou uma pessoa e eu sei falar!.')
        
julia = Pessoa('marrom', 'femea', 2, 'loiro')
    
