cashB = float(input('Valor de 1H de trabalho: '))
horaT = int(input('Horas Trabalhadas: '))

cashB *= horaT

ir = cashB * 0.11
inss = cashB * 0.08
sind = cashB * 0.05

cashL = cashB - (ir + inss + sind)

print('##### Descontos ######')
print('# INSS: %0.2f       #' %inss)
print('# SIND: %0.2f       #' %sind)
print('# IR: %0.2f         #' %ir)
print('')
print('##### Salarios #######')
print('# Bruto: %0.2f     #' %cashB)
print('# Liquido: %0.2f   #' %cashL)





    
