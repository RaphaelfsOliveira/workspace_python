import random
tam = 10
nu, ni, num = [], [], []

i = 0
while i < tam:
    nu.append(random.randrange(1,101))
    ni.append(random.randrange(1,101))
    i+=1

print(nu)
print(ni)

i = 0
while i < 10:
    print('Antes de add: ', i, num)
    num.append(nu[i])
    num.append(ni[i])
    print('Depois de add: ', i, num)
    print()
    i+=1

print(num)

