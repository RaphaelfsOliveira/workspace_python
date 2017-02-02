word = input('Digite uma palavra: ')
word_c = []
troca = ''

i = 0
while i < len(word):
    if word[i] in 'aeiou':
        word_c.append('*')
        troca += '*'
    else:
        word_c.append(word[i])
        troca += word[i]
    i+=1

to_string = ''.join(word_c)

print(word_c ,type(word_c))
print(to_string, type(to_string))

print(troca, type(troca))
