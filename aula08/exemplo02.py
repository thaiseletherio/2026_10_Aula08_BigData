produtos = []

for i in range (3):
    produto = input('Informe o nome do produto: ')
    produtos.append(produto) # .append adiciona produtos à uma lista

print (produtos)


#ACESSAR O ELEMENTO
n = int(input('Digite a posição do elemento a acessar: '))
print (produtos[n-1])

# ALTERAR uma lista "nome de um elemento"
produtos [n-1] = input(f'Informe o nome do elemento: {n} ')
print (produtos)

#REMOVER um elemento da lista
produto_a_remover = input('\n Digite o nome do produto a remover: ')
if produto_a_remover in produtos:
    produtos.remove(produto_a_remover)
print (produtos)

# métodos: insert (insere numa posição específica), pop (apaga pelo índice), clear (zera a lista)