#modulo time
import time

print(time.asctime(), ': Devolve uma string com dia da semana, mes, dia, hora, min, seg e ano\n')
print(time.asctime(time.localtime(1)))
#tempo = time.struct_time()


print(time.localtime(), ': retorna o horario e data local no formato struct_time\n')

ta = time.localtime()
print(ta[0])
print(ta[1])
print(ta.tm_zone, ': timezone')
print(ta.tm_gmtoff, ': segundos após Greenwich')

#pode ser usado para medir passagem de tempo com precisao
print(time.time(), ': retorna o numero de segundos que passaram desde a epoca do sistema')

ti = time.time() #muito usado para medir intervalos de tempo com fiz abaixo
#time.sleep(3)
tf = time.time()
tt = tf - ti
print(tt)

#usado tambem para medir intervalos de tempo muito curto de 
#processamentos ele marca o tempo antes e depois da execução
print(time.process_time(), ': intervalo de tempo que transcorre para um determinado processamento')


print(time.localtime(time.time()), ': recebe um intervalo de tempo e monta uma struct time a partir do tempo que voce passou e o tempo inicial definido pelo sistema')
print(time.localtime(1))
a = time.localtime(1)
print(a.tm_zone, '\n')

print(time.gmtime(), ': retorna umas struct time no meridiano de Greenwich\n')
print(time.gmtime(1))

