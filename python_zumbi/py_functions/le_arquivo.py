arquivo = open('numeros.txt', 'r') #abre o arquivo para leitura

for linha in arquivo.readlines():
    print(linha.rstrip())

arquivo.close() # fecha o arquivo


#leitura na forma pythonica

with open('numeros.txt') as f:
    print(f.read())


arquivo.readlines() #gera uma lista onde cada elemento e uma linha lida
linha.rstrip() # retira o pular uma linha da leitura
