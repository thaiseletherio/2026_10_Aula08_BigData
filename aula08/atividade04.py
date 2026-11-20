numeros = []
contador = 0

for i in range (15):
    contador = contador + 1
    numero = int(input(f'Insira um número inteiro. Inserção {contador}: '))
    numeros.append (numero)

conjunto = set (numeros)
print ('\nVocê inseriu esses números: ')
print (conjunto)