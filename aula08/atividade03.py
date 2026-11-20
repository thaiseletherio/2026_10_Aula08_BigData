inteiros = []
contador = 0

for i in range (12):
    contador = contador + 1
    numero = int(input(f'Insira um número inteiro. Inserção {contador}: '))
    inteiros.append (numero)

ordenada = sorted(inteiros)
print('\nVocê inseriu os números: ')
print (ordenada)