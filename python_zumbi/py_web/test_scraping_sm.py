import urllib.request #modulo que permite conversar com a internet
pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html')
text = pagina.read().decode('utf8')
print(text)
i = text.find('>$')
preco = text[i+2:i+6]
print('Preco: ', preco)
