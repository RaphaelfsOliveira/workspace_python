'''
pais A 80.000 hab tax 3%
pais B 200.000 hab tax 1.5%
'''

a = 80.000
b = 200.000
ano = 0

while a < b:
    a *= 1.03
    b *= 1.015
    ano += 1

print('Pais A vai ultrapassar B em %d anos' %ano)
    
    
    
    


        
