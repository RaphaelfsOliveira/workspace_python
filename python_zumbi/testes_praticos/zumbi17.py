arq = open('alice.txt')
text = arq.read()
text = text.lower()
import string
for c in string.punctuation:
    text = text.replace(c, ' ')
text = text.split()

dic = {}
for w in text:
    if w not in dic:
        dic[w] = 1
    else:
        dic[w] += 1

print('Alice aparece %s vezes' %dic['alice'])
arq.close()


