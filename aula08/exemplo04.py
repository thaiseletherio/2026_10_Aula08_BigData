# # set "conjunto"
# coleção mutável
# não garante ordem
# Não há índice
# Não aceita repetição / elementos duplicados

#CRIAR sets vazios
# dias = set ()
# dias.add ('segunda')
# dias.add ('terça')
# print (dias)

# Conjuntos inicializados
# frutas = {'maçã', 'uva', 'pera', 'laranja'}
# print (frutas)
# print (type(frutas))

# remover
# frutas.remove ('uva')
# frutas.discard ('uva')
# print (frutas)
# print (len(frutas))

#converter lista para sets
# lista = [5, 7, 4, 1, 2, 8, 13, 6]
# conjunto_set = set (lista)
# print(conjunto_set)

numeros = [5, 7, 4, 1, 2, 8, 13, 6, 6, 4, 29, 5, 5]
conjunto = set (numeros) # converter lista para conjunto set
numeros = list(conjunto) # converter conjunto set para lista
print (len(conjunto))
print(conjunto)

