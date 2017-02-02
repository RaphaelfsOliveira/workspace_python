import urllib.request
pagina = urllib.request.urlopen(
    'http://www.prezunic.com.br/Ofertas.aspx?tipo=Oferta%20do%20dia&&Area=Ofertas'
    '''http://beans.itcarlow.ie/prices.html''')
text = pagina.read().decode('utf8')
print(text)
preco = text[234:238]
print('Preco: ', preco)
