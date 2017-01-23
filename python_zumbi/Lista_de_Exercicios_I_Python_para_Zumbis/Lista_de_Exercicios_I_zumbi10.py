f_dia = int(input('Quantidade de cigarros fumados por dia: ')) * 600
f_anos = int(input('Quantos anos já fumou: ')) * 365
perda = (f_dia * f_anos) // 86400
print('O Fumante perdeu:', perda, 'dia(s) de vida')
