fib = int(input('Digite um numero: '))
fib_list = [1,1]

i = 0
while i <= fib:
    #print(fib_list[i]+fib_list[i+1], )
    fib_list.append(fib_list[i]+fib_list[i+1])
    i += 1
    
num_fib = fib_list[fib-1]
print('Fibonacci: %d '%num_fib)
print()
print('Lista de Fibonacci:', fib_list)
    



    
    
    
    
    
    


        
