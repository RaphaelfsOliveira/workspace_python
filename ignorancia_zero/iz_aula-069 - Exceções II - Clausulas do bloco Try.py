# clausulas para o bloco try

try:
    lista = []
    lista.append(int('dsdsad'))
except IndexError:
    print('erro')
except ValueError:
    print('deu erro de valor')
finally:
    print('Chegamos ao final')
