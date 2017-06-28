
#qual o criterio para um objeto ser percorrido por um for loop

#objeto iteravel -> objeto capaz de gerar um objeto iterador

#bloco iteradores while e for
#for loops = iteração

'''
Objeto iterador seria uma lista ou um objeto que gera resultados a cada vez que voce o percorre.

metodos do objeto iterador

__next__ = metodo especial ou magico
chama o metodo next do objeto

__iter__ = metodo que gera iterador
chama o metodo que gera um objeto iterador
'''


file = open('itera.txt', 'w')
file.write('ola\n')
file.write('está é a aula de iteração\n')
file.write('Espero que voce esteja entendendo\n')
file.write('vamos dar continuidade')
file.close()


x = open('itera.txt', 'r')

for i in x:
    print(i)

x.close()


'''chamar o arquivo com o iterador é comparavel a uma função C
enquanto fazer um for no arquivo proporciona perda de desempenho'''

for i in open('itera.txt').readlines():
    print(i)
    


