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
    #print('Isolando palavra: ', text_clean[i].lower())
    j=0
    py = 'python'
    while j < len(py):
        if  py[j] in text_clean[i].lower() and len(text_clean[i].lower()) > 4:
            print(py[j], text_clean[i].lower())
            python_list.append(text_clean[i].lower())
            break
        j+=1    
    i+=1

print(python_list)

