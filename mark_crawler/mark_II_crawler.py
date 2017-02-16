from urllib import request, parse, error
import string

url = 'http://www.epocacosmeticos.com.br/'

def search_urls(url):
	
	try:
		pag = request.urlopen(url)
	except HTTPError as e:
		content = e.read()

	text = pag.read().decode('utf8')

	#string.punctuation
	for c in '><':
		text = text.replace(c, ' ')
	text = text.split()
	#print(text)
	
	l_type = list()

	for word in text:

		if word.lower().startswith('href'):
			l_word = word.replace('href=', '').replace('"', '')
			#p_word = parse.urlparse(l_word)
			l_type.append(l_word)
			
	return l_type


if __name__ == '__main__':

	print()

	links = search_urls(url)
	links2 = []

	#print(links)

	for link in links:
		if link.startswith('http'):
			#print(link)
			links2 = search_urls(link)

		

	