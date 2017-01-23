na = int(input('Digite n1: '))
nb = int(input('Digite n2: '))

def mdc(a, b):
    if b <= 1:
        #print(a,b)
        return a
    else:
        #print(b, a%b)
        return mdc(b, a % b)

print(mdc(na, nb))


    
    
    


        

