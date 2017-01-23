s = float(input('Digite seu salario: '))
a = float(input('Porcentagem de aumento: ')) / 100
a *= s
s += a
print('O aumento foi de: %.2f'%a)
print('Novo salario: %.2f' %s)
