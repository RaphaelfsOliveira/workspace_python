'''Converta uma temperatura digitada em
Celsius para Fahrenheit. F = 9*C/5 + 32'''

fah = float(input('Temperatura em Celcius: '))
fah = (fah * 9/5) + 32
print('Temperatura em Fahrenheit: %.1f' %fah)
