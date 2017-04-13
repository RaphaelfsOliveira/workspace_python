# break # parar ou interromper loops
# continue # continuar loops imediatamente, não executa o resto do codigo

for i in range(10):
    if i == 5:
        continue
    print(i)



'''
def cria_lista():
    lista = []

    m = int(input('Digite o tamanho da lista: '))

    for i in range(m):
        e = float(input('Digite o elemento %i de %i: ' %(i+1, m)))
        lista.append(e)

    return lista

def main():
    l1 = cria_lista()

    n = int(input('Digite o numero de elementos que se deseja somar: '))

    soma = 0
    for i in range(len(l1)):
        if i == n:
            break
        soma += l1[i]

    print('A soma é: ', soma)

main()
'''

    



    
