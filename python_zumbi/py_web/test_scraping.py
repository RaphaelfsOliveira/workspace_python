import urllib.request #modulo que permite conversar com a internet
pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html')
text = pagina.read().decode('utf8')
print(text)
preco = text[234:238]
print('Preco: ', preco)
