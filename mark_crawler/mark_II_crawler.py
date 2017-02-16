from urllib import request, parse
import string

url = 'http://www.epocacosmeticos.com.br/'
link_i = 'departamentos'
link_f = 'ofertas'


def search_urls(url, link_i, link_f):
	
	pag = request.urlopen(url)
	text = pag.read().decode('utf8')

	#string.punctuation
	for c in '><':
		text = text.replace(c, ' ')
	text = text.split()
	#print(text)

	l_type = {}
	cap = False

	for word in text:

		if 'href' in word.lower():
			l_word = word.replace('href=', '').replace('"', '')
			p_word = parse.urlparse(l_word)
			l_type[p_word.path] = p_word.geturl()
			#print('URL: ', p_word.geturl())
			
			

	return l_type

if __name__ == '__main__':

	print()

	dictt = search_urls(url, link_i, link_f)

	for key in dictt:
		print('chave [ %s ] = %s' %(key, dictt[key]))
		print()
'''
	for key in dictt.values():

		url = key
		dict2 = search_urls(url, 'categorias', 'botao-submenu')

	for key in dict2:
		print('chave [ %s ] = %s' %(key, dict2[key]))
		print()
'''
#print(dictt.values())

