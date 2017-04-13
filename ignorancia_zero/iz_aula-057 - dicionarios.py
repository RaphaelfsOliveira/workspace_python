
contato = {'Nome': 'Pedro',
           'Telefone': 123456,
           'Celular': 123456,
           'Email': 'pedro@email.com',
           'Endereço': 'Av. das Américas'}

contato = contato2.copy() #cria uma copia independente do dicionario
contato.pop() # retorna o valor e elimina a chave no parametro
contato.popitem() # elimina a primeira chave e retorna uma tupla com chave e valor
contato2.clear() # elimina todas as chaves e valores do dicionario
contato.setdefault() #retorna o valor se a chave no parametro existir se não cria a chave com valor vazio ou especificado no argumento


