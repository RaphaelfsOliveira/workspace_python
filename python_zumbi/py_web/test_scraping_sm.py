import urllib.request #modulo que permite conversar com a internet
#import string
pagina = urllib.request.urlopen(
    'http://www.prezunic.com.br/Ofertas.aspx?tipo=Oferta%20do%20dia&&Area=Ofertas')
text = pagina.read().decode('utf8')
#print(text)
preco = ''
prod = ''
produto = dict()
lista_preco = []
lista_prod = []

for c in '!"#%&\'()*+-/:;<=>?@[\\]^_`{|}~':
    text = text.replace(c, ' ')

text = text.split()
#print(text)
for t in text:
    if 'R$' in t:
        produto['sem produto'] = t
    if 'nomeProd' in t:
        produto[t] = 'sem preco'
    #produto[prod] = preco

for t in text:
    if 'R$' in t:
        lista_preco.append(t)
    if  t.startswith('nomeProd'):
        #i = text.index(t)
        #t = text[i+1] + ' ' + text[i+2] + ' ' + text[i+3]
        lista_prod.append(t)


for i in range(len(lista_prod)):
    print(lista_prod[i], lista_preco[i])

for t in text:
    if t.startswith('nomeP'): print(t)
    if 'R$' in t: print(t)

print(produto)
