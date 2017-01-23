dist = int(input('distancia da viajem: '))
vel = int(input('Velocidade media: '))
# 100 km -> 60 km/h
h, m = dist // vel, dist % vel
print('A viagem vai demorar:', h, 'hora(s) e', m, 'minuto(s)')
