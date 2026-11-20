vendas = []

contador = 0
for i in range (10):
    contador = contador + 1
    valor = float(input (f'Qual o valor da venda {contador}: R$' ))
    vendas.append (valor)

print (vendas)
total = sum(vendas)
print (f'Total de vendas: {total}')
