# modulo json
# java script object notation serializer = json
import json

data = {'Nome': 'Pedro', 'RG': 123456789, 'CPF': 1234567890}
data_string = json.dumps(data)
#print(data_string)

file = open('test.json', 'ab')
file.write(data_string.encode())
file.write(json.dumps([1, 2, 3, 4]).encode())
file.write(json.dumps(('a', 'b', 'c')).encode())
file.close()

#lendo o arquivo
file = open('test.json', 'rb')
data_total = file.readlines()
file.close()
data2 = data_total[54:66]
data2 = data2.decode()
obj2 = json.loads(data2)
print(obj2)
