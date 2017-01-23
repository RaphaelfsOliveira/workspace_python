import string
string.punctuation

text = 'Alice foi atrás do coelho, mas não o encontrou'
text = text.lower()
print(text)

text = text.replace(',', ' ')
text = text.split()

dic = {}

for w in text:
    if w not in dic:
        dic[w] = 1
    else:
        dic[w] += 1



