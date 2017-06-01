import struct

ord('a') #converte a string para byte

for c in 'palavra':
    ord(c)

x = b'palavra' # coloca a string em formato de byte


nome = 'joao'
idade = 23
altura = 1.75

#empacota as variaveis em uma struct de bytes
cod = struct.pack('4s I f' ,nome.encode(), idade, altura)

arq = open('pessoas.cod', 'wb') # salva o arquivo codificando em formato de bytes
arq.write(cod)
arq.close()

arq = open('pessoas.cod', 'rb')
cod_ab = arq.readline()
print(cod_ab)
#desempacota o codigo em struct
cod_desp = struct.unpack('4s I f', cod_ab)
print(cod_desp)
nome = cod_desp[0].decode()
print(nome)
print('##################\n')


#colocando as variaveis dentro da tupla pra empacotar mais facilmente
t = (b'Joao', 23, 1.75)
s = struct.Struct('4s I f')
data = s.pack(*t)
print(data)
