arquivo = open('mensagem.txt', 'r') #abre o arquivo para leitura
char = ''

for linha in arquivo.readlines():
    char += linha 
    print(linha.rstrip())

arquivo.close() # fecha o arquivo

arquivo = open('cripto.txt', 'w')

for c in char:
    if c in 'aeiou':
        arquivo.write('*')
    else:
        arquivo.write(c)

arquivo.close()

with open('cripto.txt') as t:
    print(t.read())



#leitura na forma pythonica
'''
with open('numeros.txt') as f:
    print(f.read())
'''

# arquivo.readlines() #gera uma lista onde cada elemento e uma linha lida
# linha.rstrip() # retira o pular uma linha da leitura
