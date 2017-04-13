'''
modo de abertura de arquivo
'w' -> write, escrever
'r' -> read, ler
'a' -> append, extender
'''
'''
########## escrevendo o arquivo
arquivo = open('test_arquivo.txt', 'w') # abrindo o arquivo

arquivo.write('chocolate\n') # escrever no arquivo '\n' <- pular linha
arquivo.write('manga')

# arquivo.writelines(['ola', 'teste', 'lista', 'de', 'arquivos']) #escrever lista

arquivo.close()
'''
'''
######## lendo arquivo
arquivo = open('test_arquivo.txt', 'r')

#x = arquivo.read()

print(arquivo.readline()) # ler uma linha e parar leitura

x = arquivo.readlines() # ler linha por linha e colocar em uma lista
print(x)

#print(arquivo.read())
arquivo.close()
'''
####### adicionando mais linhas no arquivo

arquivo = open('test_arquivo.txt', 'a')

arquivo.write('\nmais uma linha')

arquivo.close()













