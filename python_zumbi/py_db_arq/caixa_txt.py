from caixa_banco import *
import caixa_desconto
import caixa_desconto_japa

itens = ['Bauru', 'X Salada', 'Calafrango', 'Pastel']
precos = [2.50, 3.20, 2.75, 1.80]
rodando = True

while rodando:
	opcao = 1
	for escolha in itens:
		print(str(opcao) + '. ' + escolha)
		opcao += 1
	print(str(opcao) + '. Finalizar')
	escolha = int(input('Escolha uma opcao: '))
	if escolha == opcao:
		#escolheu a ultima opção
		rodando = False
	else:
		cartao = input('Numero do cartão de crédito: ')
		preco = caixa_desconto.desconto(precos[escolha - 1])
		if itens[escolha - 1] == 'Pastel':
			preco = caixa_desconto_japa.desconto(preco)
		salva_transacao(preco, cartao, itens[escolha - 1])

		