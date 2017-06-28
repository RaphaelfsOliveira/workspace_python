#construindo objetos que implementem metodos de iteração
#__iter__ --> __next__

'''
class Quadrados(object):
	
	def __init__(self, com, fim):
		self.com = com
		self.fim = fim
	
	def __iter__(self):
		#return self
		return Quadrados_iter(self.com, self.fim)
	
	def __next__(self):
		if self.com < self.fim:
			self.com += 1
			return self.com**2
		else:
			raise StopIteration

class Quadrados_iter(object):
	def __init__(self, com, fim):
		self.com = com
		self.fim = fim

	def __next__(self):
		if self.com < self.fim:
			self.com += 1
			return self.com**2
		else:
			raise StopIteration


x = Quadrados(0, 5)

for i in x:
	print(i)

for b in x:
	print(b)

print(list(x))
'''

#implementação com geradores talvez a melhor

class Quadrados4(object):

	def __init__(self, com, fim):
		self.com = com
		self.fim = fim

	def __iter__(self):
		for i in range(self.com + 1, self.fim + 1):
			yield i**2

x = Quadrados4(0, 5)

for i in x:
	print(i)

for b in x:
	print(b)

print(list(x))
print(list(x))