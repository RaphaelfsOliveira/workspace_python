import urllib.request
import json

url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'

resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf8'))

print(data['value']['joke'])
print()
print(data['value']['id'])
print()
for d in data['value']:
    print(d)
print()
print(data)
