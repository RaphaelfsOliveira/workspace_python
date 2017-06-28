#compressão de lista = forma de gerar uma lista
#list comprehesion

#formato geral
l = [x + 10 for x in range(10)]

#x + 10 --> expressão
#for x in range(10) --> for loop
#range(10) -- objeto iteravel

#### - mais rapidos que alguns loops
#### - sintaxe simples
#### - velocidade de C
'''
a = open('itera.txt')
l = a.readlines()
l = [linha.rstrip() for linha in l] # para remover o '\n' e criar a lista com mais facilidade e rapidez
'''

#mas ainda tem uma maneira mais eficiente com relação a memoria e processamento
l = [linha.rstrip() for linha in open('itera.txt')]

################################
## list comprehension com IF ###
import random

l = [random.randint(1,100) for i in range(30) if i%2==0]
l = [x for x in l if x%2==0] #escolhendo somente os numero pares

#dois for loops
l = [x + y*2 for x in 'abc' for y in 'xyz']

print(l)

