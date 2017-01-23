n1 = int(input('Numero: '))
n2 = int(input('Numero: '))
n3 = int(input('Numero: '))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n3:
    maior = n2
else:
    maior = n3

print('Maior: %d' %maior)
    
