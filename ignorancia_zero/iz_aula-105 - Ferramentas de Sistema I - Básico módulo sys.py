#modulo sys
'''
CONSTANTES
plataform = devolve o tipo de sistema que o usuário está usando
'''
import sys, os

print(sys.platform) #retorna a plataforma do sistema
'''
if 'win' in sys.platform:
	import winsound
'''
sys.path.append('C:\\')
print(sys.path) #retorna listas de pastas onde eu posso procurar arquivos

#fecha seu programa
print(sys.exit) 

#mostra os modulos utilizados pelo programa
print(sys.modules) 

#retorna uma tupla da ultima excessão levantada pelo seu programa
print(sys.exc_info()) 


