peso = float(input('Kg de peixe: '))
excesso = 0
multa = 0

def print_em():
    print('Excesso KG: %0.2f' %excesso)
    print('Multa R$: %0.2f' %multa)

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print_em()
else:
    print_em()
    
