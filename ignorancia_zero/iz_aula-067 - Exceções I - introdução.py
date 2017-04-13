'''
try:
    x = int(input('Digite um numero: '))
except:
    print('Deu erro!!')
    x = 0
finally:
    print(x)
'''



try: #tenta executar uma ação
    arq = open('arquivo.txt', 'r')
    linha = arq.readline()
    linha.split('!')
    linha = linha[0]
    arq.close()
    arq = open('arquivo.txt', 'a')
    arq.write(linha)

except FileNotFoundError: #pega a exceção e trata
    print('deu erro!!')
    arq = open('arquivo.txt', 'w')
    arq.write('Erro!!!')
    
finally: #depois de tudo executa essa ultima ação
    arq.close()
