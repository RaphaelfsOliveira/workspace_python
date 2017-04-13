arq = open('test.txt', 'w')
arq.write('Olá\n')
arq.write('Meu\n')
arq.write('Nome\n')
arq.write('é\n')
arq.write('Pedro\n')
arq.close()

arq = open('test.txt', 'r')
arq.seek(8) # pula os primeiros bytes do arquivo, começa a ler deste
arq.readline()
arq.readline()
arq.tell() # indica em que byte voce parou a leitura
arq.read(1) # o numedo dentro indica o numero de bytes que voce quer ler
arq.readline(1)
arq.readlines(1)
arq.close()


arq = open('test.txt', 'r')
for l in arq:
    print(l)
arq.close()

eval('[1, 2, 3]') # avalia a expressão e converte






