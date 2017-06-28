#iteração outros objetos iteraveis

#help(zip) objeto zip
#o objeto zip faz combinações ate o primeiro stop iterator

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
a = zip(l1, l2, l3)

print(a)

print(list(a))
print('\n')

la = ['ovos', 'presunto', 'frango']
lb = [5.30, 16.90, 26.50]

b = zip(la, lb)

#dict(b)
#print(list(b))

#help(map) objeto map
#precisa de uma funcao e os iteradores
# a vantagem de map e que podemos passar qualquer função para ele executar

l = [x**2 for x in range(10)]
l1 = map(lambda x: x**2, range(10))
l2 = map(lambda x,y: x + y, range(4), range(3, -1, -1))


#help(filter)
# recebe uma funcao ou nada e devolve um objeto filter
# para cenarios que o map não atende como voce deseja

a = filter(lambda x: x%2==0, range(5))
print(a)
print(list(a))




