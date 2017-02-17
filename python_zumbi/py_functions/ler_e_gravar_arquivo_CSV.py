import csv

arq_name = "test" 

title = 'perfumes'
name_prod = 'perfume-feminino'
url_prod = 'http://www.epocacosmeticos.com.br/perfumes/perfume-feminino'

rows = ['teste','teste']

def save_urls(arq_name, rows):
	arq = csv.writer(open(arq_name + '.csv', "w"))
	arq.writerow(rows)
	print(rows)

#print(arq)
