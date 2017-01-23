import random

num = []
maior, menor = 0, 100

i = 0
while i < 10:
    num.append(random.randrange(1,101))
    i+=1

print(num)

i = 0
while i < 10:
    if num[i] > maior:
        maior = num[i]
    if num[i] < menor:
        menor = num[i]
    i+=1

print('Maior: ', maior)
print('Menor: ',menor)
