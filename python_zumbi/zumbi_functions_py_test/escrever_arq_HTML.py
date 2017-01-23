arquivo = open('ola.html', 'w', encoding='utf-8')
arquivo.write('''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Página Python</title>
</head>
<body>
Olá! teste escrita em arquivo
</body>
</html>''')
arquivo.close()

test = ''
char = ''

with open('ola.html', encoding='utf-8') as h:
    for line in h:
        test += line
    print(h.read())

arq = open('ola.html', encoding='utf-8')
for line in arq.readlines():
    char += line
    print(line.rstrip())

char = char.split('\n')
test = test.split('\n')

