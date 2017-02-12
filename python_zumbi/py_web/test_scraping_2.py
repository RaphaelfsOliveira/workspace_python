import urllib.request #modulo que permite conversar com a internet
pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html')
text = pagina.read().decode('utf8')
print(text)
i = text.find('>$')
preco = float(text[i+2:i+6])

if preco < 4.74:
    print('Em Promoção: ', preco)
else:
    print('Está Caro!!: ', preco)
