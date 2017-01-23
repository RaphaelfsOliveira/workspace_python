ano = int(input('Digite o ano: '))

def ano_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        print('Ano bissexto!!')
        return True
    elif ano % 4 == 0 and ano % 400 == 0:
        print('Ano bissexto!!')
        return True
    else:
        print('Ano NÃO bissexto!!')
        return False

print(ano_bissexto(ano))
    
