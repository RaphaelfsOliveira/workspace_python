text = input('Text: ')
text_clean = ''

i=0
while i < len(text):
    if text[i].isalpha():
        #print(text[i], 'ok')
        text_clean += text[i]
    elif text[i] == ' ':
        text_clean += ' '
        #print(text[i], 'espaço')
    else:
        text_clean += ''
    i+=1

print(text_clean)
text_clean = text_clean.split(' ')
print(text_clean)

'''
i = 0
while i < len(text):
    if text[i] in 'python':
        print(text[i], 'word OK')
    else:
        print(text[i],'error')
    i+=1
'''

'''
print('python' in text.lower())
print(text.find('Python'))
   

cont=0
i=0
while i < len(text):
    if text.lower() in "python":
        cont+=1
    i+=1
    
print(i)
print('Contador Python: ', cont)

print(text.lower())



text = text.split(' ')

print(text)


resp = 'nao yes no'

print(resp.lower() in 'sim nÃo yes no')
'''
