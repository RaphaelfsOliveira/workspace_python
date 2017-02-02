data = input('Data de Nascimento: ')
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
       'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

data = data.split('/')
m = int(data[1])

i=1
while i < len(mes):
    if i == m:
        print('test_comparar_mes: ', i, data[1], mes[i-1])
        data[1] = mes[i-1]
    i+=1
    
print(data)
ext = ' de '.join(data)
print(ext)
