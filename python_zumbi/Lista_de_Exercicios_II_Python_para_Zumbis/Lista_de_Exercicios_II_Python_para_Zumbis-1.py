print('Digite os lados do Triangulo: ')
a = int(input('A:'))
b = int(input('B:'))
c = int(input('C:'))

def check_tri(a, b, c):
    if abs(a - b) < c and c < abs(a + b):
        if abs(b - c) < a and a < abs(b + c):
            if abs(a - c) < b and b < abs(a + c):
                return True           
    else:
        return False

def type_tri(checkTri):
    if  checkTri == True:
        #print('Type_tri_True')
        if a == b and b == c:
            print('Triangulo equilátero')
        elif a == b or b == c or a == c:
            print('Triangulo isósceles')
        else:
            print('Triangulo escaleno')
            
print(check_tri(a, b, c))
bo = check_tri(a, b, c)
type_tri(bo)
