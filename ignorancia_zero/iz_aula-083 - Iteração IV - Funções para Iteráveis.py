#funções para objetos iteraveis

'''
all, any, sum e reduce
reduce --> functools
'''

# all do ingles tudo verifica se todos os elementos de uma sequencia são verdadeiros

all([0,1,0,1,0,0])

#implementação da funcao all
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


 
#any do ingles algum verifica se pelo menos algum elemento da lista é verdadeiro

any([0,1,0,1,0,0])

#implementação da funcao any
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False



#sum função soma somente soma numeros inteiros ou floats

sum([1,5,7,4.5,5464])

s = sum([1,2,4], 7)




#reduce recebe uma funcao e recebe iteraveis
#reduce caiu em desuso porque o for loop e muito mais usado
import functools

def olhe_soma(x, y):
    print('Adicionando', x, 'a', y)
    return x + y

print(functools.reduce(olhe_soma, [1, 2, 3, 4, 5]))
