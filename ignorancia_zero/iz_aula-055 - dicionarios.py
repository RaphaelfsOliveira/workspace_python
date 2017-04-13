dic = {'Lambda': lambda x: x + 1}

contato = {'Nome': 'Pedro',
           'Telefone': 123456,
           'Celular': 123456,
           'Email': 'pedro@email.com',
           'Empresa': 'StartupMan'}

for key in contato:
    print(key, '->', contato[key])

print('\n')
print('Endereco' in contato)
print(len(contato))
