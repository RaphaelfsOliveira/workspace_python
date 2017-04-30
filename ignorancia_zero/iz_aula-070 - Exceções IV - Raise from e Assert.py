# raise from e assert
'''
try:
    num = 1 / 0
    int(num)
except Exception as E:
    raise ValueError from E
''' 

while True:
    try:
        num = int(input('Digite um numeor entre 1 e 20: '))
    except ValueError:
        print('Digite apenas numeros')
    except:
        print('Entrada invalida')
    else:
        break

test = True

if not 1 <= num <= 20:
    test = False

assert test, num

if __debug__:
    if not test:
        raise AssertionError(num)

def raiz(x):
    assert x > 0, 'x tem que ser maior que zero'
    return x**1/2

