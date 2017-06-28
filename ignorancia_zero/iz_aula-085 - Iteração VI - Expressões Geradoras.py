#bem parecido com listcomprehension

#list comprehension
l = [x**2 for x in range(10) if x % 2 == 0]
print(l)

#expressoes geradoras
g = (x**2 for x in range(10) if x % 2 == 0)
print(g)

print(iter(l) is l) #a lista é um objeto iteravel mas nao é um objeto iterador

print(iter(g) is g) #ja a expressao geradora é iteravel e iterador

'''
compressao de lista é mais veloz que expressoes geradoras

Então qual a vantagem ?!?!?

a lista ja armazena os inteiros na memoria 
ja no objeto gerador somente é armazenado o objeto gerador 
então em algum casos cabe melhor um ou outro

compressao de listas é melhor para processamento
expressao geradora ocupa menos memoria
logo cada um serve para um caso...
'''
print('\nExpressao Geradora')
for i in g:
	print(i)

#depois que a expressao já foi percorrida se tentar gerar uma lista,
#voce gera uma lista vazia
print(list(g), ': Depois que já foi iterado gera uma lista vazia pois não é iterado novamente')

# e se tentar percorer a expressão de novo ela não é mais percorrida
'''
for m in g:
	print(m)
for c in g:
	print(c)
'''
print('\nCompressao de Lista')
for i in l:
	print(i)

print(list(l), ': Mesmo depois de iterado pode ser iterado novamente e não gera uma lista vazia')

print('\nCompressao de Lista')
for p in l:
	print(p)



