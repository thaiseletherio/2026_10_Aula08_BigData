inteiros = []

while True:
    numero = int(input('Digite um número: '))
    parar = input('Você quer continuar? [S/N]').upper()
    inteiros.append (numero)
    print (parar)
    if parar == 'N':
        break

total = len (inteiros)
soma = sum (inteiros)
print (f' \nVocê digitou os números: ')
print (inteiros)
print (f'Total de interações: {total}')
print (f'Soma dos números inseridos: {soma}')