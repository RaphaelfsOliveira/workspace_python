def salva_transacao(preco, cartao, descricao):
	file = open('transações.txt', 'a')
	file.write('%16s%07d%16s\n' %(cartao, preco * 100, descricao))
	file.close()