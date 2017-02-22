import sqlite3

con = sqlite3.connect('alunos.bd')
curs = con.cursor()

def add_aluno(name, ra):
    query = 'insert into alunos values ("%s", %s)' %(name, ra)
    curs.execute(query)

#add_aluno('masanori', 42)
#add_aluno('emengarda', 66)
#add_aluno('astrogildo', 11)
#add_aluno('kilda', 76)
curs.execute('select * from alunos')

for x in curs.fetchall():
    print(x)

curs.close()
con.commit()
curs.close()
