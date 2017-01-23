text = input('Text: ')
text = '“The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”'
text_clean = ''
python_list = []

i=0
while i < len(text):
    if text[i].isalpha():
        text_clean += text[i]

    elif text[i] == ' ':
        text_clean += ' '

    else:
        text_clean += ''
    i+=1

print(text_clean)
text_clean = text_clean.split(' ')
print(text_clean)

i=0
word=''
while i < len(text_clean):
    #print(text_clean[i].lower())
    print('Isolando palavra: ', text_clean[i].lower())
    j=0
    py = 'python'
    while j < len(py):
        if text_clean[i].lower().startswith(py[j]) or text_clean[i].lower().endswith(py[j]):
            python_list.append(text_clean[i].lower())
            break
        j+=1    
    i+=1


print(python_list)

'''
#contar numero de palavras python
i=0
while i < len(text_clean):
    print('python' in text_clean[i].lower())
    i+=1
    
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
