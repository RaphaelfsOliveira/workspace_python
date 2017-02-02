import urllib.request #modulo que permite conversar com a internet
#import string
pagina = urllib.request.urlopen(
    'http://www.prezunic.com.br/Ofertas.aspx?tipo=Oferta%20do%20dia&&Area=Ofertas')
text = pagina.read().decode('utf8')
print(text)
preco = ''

prod = dict()

for c in '!"#%&\'()*+-/:;<=>?@[\\]^_`{|}~':
    text = text.replace(c, ' ')

text = text.rsplit()
i = 0

for t in text:
    if t.startswith('R$'):
        prod[i] = t[2:]
    if t.startswith('nomeProd'):
        prod[t]
    i += 1

for ch in prod:
    print(prod, '->', prod[ch])



'''
i = text.find('>R$')
preco.append(text[i+2:i+8])

while text.rfind('>R$') > text.find('>R$', i):
    i = text.find('>R$', i) + 1
    preco.append(text[i+1:i+8])
    
#preco = text[i+3:i+7]
print('Preco: ', preco)
'''
