d = {}
d['a'] = 'alpha'
d['o'] = 'omega'
d['g'] = 'gama'
print('Chaves: ', d.keys())
print('Valores: ', d.values())

print('a' in d) #perguntando se tem no dicionario
print('x' in d)

for chave in d:
    print(chave)
    print(chave, '->', d[chave])
