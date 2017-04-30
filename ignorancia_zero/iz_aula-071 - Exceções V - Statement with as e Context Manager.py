# with as, CONTEXT MANAGER

x = open('exce.txt', 'w')
x.write('Ola')
x.write('mundo')
x.close()

with open('exce.txt') as meu_arq:
    for line in meu_arq:
        print(line)


class nosso_context_manager(object):
    def imprime(self, msg):
        print(msg)
    def __enter__(self):
        print('entrando no bloco with')
        return self
    def __exit__(self, tipo, valor, traceback):
        print('tipo->', tipo)
        print('valor->', valor)
        print('Traceback->',traceback)

with nosso_context_manager() as teste:
    teste.imprime('Ola Mundo')
    #raise ValueError


        
        
