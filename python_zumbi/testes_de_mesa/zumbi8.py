word = input('Digite uma palavra: ')
troca = ''

i = 0
while i < len(word):
    if word[i] in 'aeiou':
        troca += '*'
    else:
        troca += word[i]
    i+=1

print(troca, type(troca))

