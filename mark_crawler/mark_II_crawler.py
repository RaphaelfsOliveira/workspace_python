from urllib import request, parse, error
import string
import csv


def search_urls(url, i_filter, f_filter):
	
	#pag = request.urlopen(url)
	pag, headers = request.urlretrieve(url)

	#text = pag.read().decode('utf8')
	html = open(pag, encoding='utf8')
	text = html.read()
	html.close()

	#string.punctuation
	for c in '><':
		text = text.replace(c, ' ')
	text = text.split()
	#print(text)
	
	l_type = list()
	capt = False	

	for word in text:

		if i_filter.lower() in word.lower():
			capt = True

		if f_filter.lower() in word.lower():
			capt = False

		if word.lower().startswith('href') and capt:
			l_word = word.replace('href=', '').replace('"', '')
			if l_word.startswith('http') and l_word not in l_type:
				#p_word = parse.urlparse(l_word)
				l_type.append(l_word)
			
	return l_type


if __name__ == '__main__':
	import operator

	url = 'http://www.epocacosmeticos.com.br/'
	i_filter = 'Departamentos'
	f_filter = 'selecao'

	print()

	links = search_urls(url, i_filter, f_filter)
	
	arq_name = "links" 
	arq = csv.writer(open(arq_name + '.csv', "w"))
	
	arq.writerow(['Titulo', 'Nome do Produto', 'URL'])
	
	for link in links:

		if len(link) > len(url):
			print('LINK Ok: ',link)
			title = link.replace('http://www.epocacosmeticos.com.br/', '').split('/')
			
			if len(title) > 1:
				title, nome_prod = title[0], title[1]
			else:
				title, nome_prod = title[0], title[0]
			
			arq.writerow([title, nome_prod, link])
		else:
			print('Error Short Link: ', link)

	print('[ FINISH LINKs ]================================================')

	for link in links:
		if 'map=c' not in link:
			links2 = search_urls(link, 'CATEGORIAS', 'CLIQUE E VEJA MAIS!')

	arq_name = "links2" 
	arq = csv.writer(open(arq_name + '.csv', "w"))

	arq.writerow(['Titulo', 'Nome do Produto', 'URL'])

	for link in links2:
		
		if len(link) > len(url):
			print('LINK Ok: ',link)
			title = link.replace('http://www.epocacosmeticos.com.br/', '').split('/')
			
			if len(title) > 1:
				title, nome_prod = title[0], title[1]
			else:
				title, nome_prod = title[0], title[0]

			arq.writerow([title, nome_prod, link])
		else:
			print('Error Short Link: ', link)

	
	print('[ FINISH LINKs 2 ]================================================')

	for link in links2:
		if 'map=c' not in link:
			links3 = search_urls(link, '/head', '/body')
	
	#link = 'http://www.epocacosmeticos.com.br/perfumes/perfume-feminino'
	#links3 = search_urls(link, '/head', '/body')

	#for link in links2:
	#	if 'map=c' not in link:
	#		links3 = search_urls(link, '/head', '/body')

	arq_name = "link_prod" 
	arq = csv.writer(open(arq_name + '.csv', "w"))

	arq.writerow(['Titulo', 'Nome do Produto', 'URL'])

	for link in links3:

		if len(link) > len(url):
			print('LINK Ok: ',link)
			title = link.replace('http://www.epocacosmeticos.com.br/', '').split('/')
			
			if len(title) > 1:
				title, nome_prod = title[0], title[1]
			else:
				title, nome_prod = title[0], title[0]
			
			arq.writerow([title, nome_prod, link])
		else:
			print('Error Short Link: ', link)

	print('[ FINISH LINKs 3 ]================================================')

