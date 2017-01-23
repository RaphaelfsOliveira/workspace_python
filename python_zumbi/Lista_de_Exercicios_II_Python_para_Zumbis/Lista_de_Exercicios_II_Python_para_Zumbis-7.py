area = int(input('Area em m2: '))

l = area / 3

lata = 0

if l <= 18:
    lata = 1
else:
    print('lata antes while: %d' %lata)
    while l > 0:
        lata += 1
        l -= 18
        print('lata + 1: %d' %lata)


custo = lata * 80
print('Lata(s): %d, Custo R$: %0.2f' %(lata, custo))





    
