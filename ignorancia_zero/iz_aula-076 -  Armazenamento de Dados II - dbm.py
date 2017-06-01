import dbm #database manager
'''modos de abertura
c -> cria o database se ele nao existir ou abre um existente
r -> le o database
w -> escreve ou le o database
n -> vai abrir um novo database para ler ou escrever
'''

db = dbm.open('contatos.db', 'c')
db['Pedro'] = 'pedro.kau@gmail.com'
db['Tel'] = '99990000'

print(db['Pedro'].decode())
print(db['Tel'].decode())

# metodos do database
len(db) 
db.keys()
print('Pedro' in db)
print(db.keys())
print('Deletando uma Chave...')
del db['Tel']
print(db.keys())
db['Tel'] = '99990000'

for key in db:
    print(key.decode(), '->', db[key])

print(db.pop('Tel'))

db.close()
    
    
