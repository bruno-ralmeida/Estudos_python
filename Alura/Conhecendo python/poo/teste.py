from conta import Conta
from cliente import Cliente

Conta.cod_banco()

conta = Conta(123, 'Bruno', 100.00, 1000.00)
conta.deposito(50)
conta.extrato()

conta2 = Conta(456, 'Ana', 150.00, 1000)

conta.transfere(125.00, conta2)
conta.extrato()
conta2.extrato()

conta2.saque(5000)


print(conta.limite)
conta.limite = 10000.95
print(conta.limite)

cliente = Cliente('bruno')
print(cliente.nome)

cliente.nome = 'irineu'
print(cliente.nome)