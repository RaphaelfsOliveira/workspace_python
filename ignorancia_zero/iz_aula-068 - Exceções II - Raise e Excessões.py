try:
    raise ValueError
except ValueError:
    print('Pegamos a excessão')

def test():
    try:
        a = int(input('Escolha um numero entre 1 e 20: '))
        if not 1 <= a <= 20 :
            raise ValueError
        else:
            print('Obrigado por escolher', a)

    except ValueError:
        print('entrada invalida')


#################### criando excessões

class ValorRepetidoErro(Exception):
    def __init__(self, n):
        self.num = n
    def __str__(self):
        return 'puts meu caro, você já digitou esse numero %s antes' %self.num
    


def test2():
    lista = []

    for i in range(3):
        while True:
            try:
                num = int(input('Escolher um numero: '))
                break
            except ValueError:
                print('Digite apenas números')

        if num not in lista:
            lista.append(num)
        else:
            raise ValorRepetidoErro(num)




if __name__ == '__main__':
    test2()
