import random
tam = 20
num, par, imp = [], [], []

i = 0
while i < tam:
    num.append(random.randrange(1,101))
    i+=1

print(num)

i = 0
while i < tam:
    if num[i] % 2 == 0:
        par.append(num[i])
    else:
        imp.append(num[i])
    i+=1

print('Par: ', par)
print('Impar: ', imp)

