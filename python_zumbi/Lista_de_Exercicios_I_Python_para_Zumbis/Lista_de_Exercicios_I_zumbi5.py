prod = float(input('Preço da Mercadoria: '))
desc = float(input('Percentual de desconto: ')) / 100
desc *= prod
prod -= desc
print('Desconto: %.2f' %desc)
print('Preco com desconto: %.2f' %prod)

