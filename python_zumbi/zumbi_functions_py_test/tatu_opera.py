from tatu_banco import *
from tatu_banco3 import ContaEspecial

jose = Cliente('Jose Augusto Silva', '7777-1234')
maria = Cliente('Maria de Albuquerque', '8888-1234')

print('Nome: %s, Telefone: %s' %(jose.nome, jose.telefone))
print('Nome: %s, Telefone: %s' %(maria.nome, maria.telefone))
conta1 = Conta([jose], 1, 1000)
conta2 = ContaEspecial([maria, jose], 2, 500, 1000)
conta1.resumo()
conta2.resumo()
print()
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()



