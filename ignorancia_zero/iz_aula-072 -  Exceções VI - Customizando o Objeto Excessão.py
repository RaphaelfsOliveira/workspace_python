## customizando o objeto excessão
'''
class NossoContextManager(object):
    def __enter__(self):
        print('entramos no blco with')
        return self
    def __exit__(self, tipo, valor, traceback):
        print(tipo)
        print(valor)
        print(traceback)

	
with NossoContextManager() as nosso:
    raise ValueError('spam')


class DeuErro(Exception):
	pass


raise DeuErro('Puts cara deu erro justo agora')

'''

class DeuErroArquivo(Exception):
    def __init__(self, linha, arq):
        self.linha = linha
        self.arq = arq
    def __str__(self):
        return 'Deu erro na linha\n%s\ndo arquivo %s'%(self.linha, self.arq)
    
