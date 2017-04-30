# clausulas para o bloco try

try:
    lista = []
    lista.append(int('1'))
except (IndexError, ValueError) as excessao:
    print(excessao)
    print('erro')
else:
    print('sem excessoes')
except:
    print('Deu erro!!')
finally:
    print('Chegamos ao final')
