# metodo especial construtor de objeto

# instancia o objeto
'__init__' 

# devolve o objeto no formato de um dicionario
'__dict__'

# transforma o objeto em string, tem sempre que retornar uma string
'__str__' 

# faz operações com outra instancia do objeto somente com sinal + - / *
'__add__'

#imprime na tela a documentação escrita na classe do objeto instanciado
'__doc__'



class Conta(object):
    '''O Objeto conta representa uma conta de banco'''
    def __init__(self, ID, saldo):
        '''metodo construtor do objeto'''
        self.ID = ID
        self.saldo = saldo
    def __str__(self):
        '''transforma o objeto em string'''
        return 'ID: %d\nSaldo R$: %.2f' %(self.ID, self.saldo)
    def __add__(self, outro):
        '''faz operações com outra instancia do objeto somente com sinal + - / *'''
        self.saldo += outro.saldo
    def __call__(self, x):
        '''torna o objeto chamavel para realizar alguma operação'''
        return x
    



bra = Conta(123, 5000)
ita = Conta(456, 8000)

print(bra.__dict__, '__dict__ devolve o objeto como dicionario')
print(bra.__doc__, '__doc__ documentação da classe do objeto')


'''
>>> class Pai:
	pass

>>> class Filho(Pai):
	pass

>>> class Neto(Filho):
	pass

>>> issubclass(Pai, Filho)
False

>>> issubclass(Filho, Pai)
True

>>> Filho.__bases__
(<class '__main__.Pai'>,)

>>> Neto.__bases__
(<class '__main__.Filho'>,)

'''
