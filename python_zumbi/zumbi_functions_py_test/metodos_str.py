#ver todos os metodos de uma string
dir(str)

# saber o que o metodo faz
help(str.isalpha())

arq = 'prog.py'
print(arq)
print('Metodo começa com: ', arq.startswith('p'))#metodo começa com
print('Metodo termina com: ', arq.endswith('y'))#metodo string termina com
print()

resp = "Sim"
print(resp)
print('Metodo lower: ', resp.lower())#coloca toda string em minusculo
print('Metodo upper: ', resp.upper())#coloca toda string em maiusculo
print()

print(resp.lower() in 'sim nao yes no')#verifica se tem a str em minusculo no texto

s = 'um tigre, dois tigres, tres tigres'
s.find('tigre')#procura uma string dentro do texto
s.find('tigre', 4)#procura a partir do indice que voce informar
s.find('tigre', 16)

s.replace('tigre', 'gato') # faz uma copia da string e mostra a copia
print(s)
s = s.replace('tigre', 'gato') # tem que atribuir para trocar na str original
print(s)


#split and join
#split
txt = 'batatinha quando nasce'
txt.split() #separa uma string em uma lista

data = '21/02/2011'
data.split('/')

ip =  '192.168.0.98'
ip.split('.')
#>>> ['192', '168', '0', '12']

#join
times = ['Vasco', 'Botafogo', 'Fluminense']#junta listas ou strings
'-'.join(times)
#>>> 'Vasco-Botafogo-Fluminense'












































