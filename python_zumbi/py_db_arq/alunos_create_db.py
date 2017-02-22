import sqlite3

con = sqlite3.connect('alunos.bd')
curs = con.cursor()
curs.execute('''create table alunos(
                        login varchar(8),
                        ra integer
                        )''')
curs.close()
con.close()
