import csv

arq_name = "test2" 

title = 'perfumes'
name_prod = 'perfume-feminino'
url_prod = 'http://www.epocacosmeticos.com.br/perfumes/perfume-feminino'
rows = [title, name_prod, url_prod]





arq = csv.writer(open(arq_name + '.csv', "w"))

for i in range(10):
	arq.writerow([title, name_prod, url_prod])

arq.writerow(rows)

	
arq_r = csv.reader(open(arq_name + '.csv'))
#arq_r = csv.reader('test', delimiter=' ', quotechar='|')

for row in arq_r:
	print(row)

with open(arq_name + '.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ', quotechar='|')

	for row in reader:
		print(', '.join(row))

		