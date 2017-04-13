# comparação de objetos

class Conta(object):
    def __init__(self, i, s):
        self.ID = i
        self.saldo = s
    def deposito(self, v):
        self.saldo += v
        print('Deposito OK')
    def saque(self, v):
        if self.saldo >= v:
            self.saldo -= v
            print('Saque OK!')
        else:
            print('Saldo insuficiente..')
    def __le__(self, i):
        if self.ID <= i.ID:
            return True
        return False
    def __eq__(self, i):
        if self.ID == i.ID:
            return True
        return False
    def __ge__(self, i):
        if self.ID >= i.ID:
            return True
        return False
    def __lt__(self, i):
        if self.ID < i.ID:
            return True
        return False
    def __gt__(self, i):
        if self.ID > i.ID:
            return True
        return False
    def __ne__(self, i):
        if self.ID != i.ID:
            return True
        return False
        

# metodos de comparação entre objetos
'__le__' # x <= y
'__eq__' # x == y
'__ge__' # x >= y
'__lt__' # x < y
'__gt__' # x > y
'__ne__' # x != y


'''        
>>> ita3 = ita
>>> ita3.deposito(6)
Deposito OK
>>> ita.saldo
7006
>>> ita3.saldo
7006
>>> ita == ita3
True
>>> id(ita)
2506222342096
>>> id(ita3) # verifica o endereço do objeto
2506222342096
>>> id(ita) == id(ita3) # as duas variaveis apontam pro mesmo objeto
True
>>> 
'''

# extender Objetos

class Banco(object):
    def __init__(self):
        self.contas = []



