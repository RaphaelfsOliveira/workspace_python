import urllib.request #modulo que permite conversar com a internet

preco = 5.0
while preco >= 4.74:
    pagina = urllib.request.urlopen(
     'http://beans.itcarlow.ie/prices-loyalty.html')
    text = pagina.read().decode('utf8')
    i = text.find('>$')
    preco = float(text[i+2:i+6])
print('Em Promoção: ', preco)
#o programa assim pode gerar DDOS
