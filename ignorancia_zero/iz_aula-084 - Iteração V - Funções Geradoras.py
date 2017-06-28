#funcoes geradoras

# yield
#objeto gerador --> possui o protocolo de iteração --> iteravel --> iterador --> __next__()

def gera_quadrados(n):
    for i in range(n):
        yield i**2


def imprime(n):
    for i in range(n):
        x = yield i**2
        print(x)


z = imprime(5)
z.send(5) # envia um numero para a função pode ser um codigo de parada ou algo do tipo
 
