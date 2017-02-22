import sqlite3

db = sqlite3.connect('surfersDB.sdb')
db.row_factory = sqlite3.Row
curs = db.cursor()
query_age = '''select name, average from
                  surfers where age > 20
                  order by average desc'''
query = 'select * from surfers where age > 25'
curs.execute(query_age)
linhas = curs.fetchall()

for linha in linhas:
        print('Nome    : ', linha['name'])
        #print('País    : ', linha['country'])
        print('Média   : ', linha['average'])
        #print('Prancha : ', linha['board'])
        #print('Idade   : ', linha['age'])
        print()
curs.close()
