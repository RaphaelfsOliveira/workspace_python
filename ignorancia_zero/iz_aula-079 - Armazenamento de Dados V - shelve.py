import shelve

db = shelve.open('shelve.db')
print(db)

db['lista'] = [1, 2, 3, 4]

class Pessoa:
    pass

pedro = Pessoa()

db['pessoa'] = pedro
print(db['pessoa'])
db.close()

#adicionando um numero na lista
db = shelve.open('shelve.db')
x = db['lista']
x.append(5)
db['lista'] = x
print(db['lista'])
db.close()

#abre o db para poder escrever direto com o
#atributo append mas deixa o arquivo mais lento
db = shelve.open('shelve.db', writeback=True)
db['lista'].append(6)
print(db['lista'])
db.close()
