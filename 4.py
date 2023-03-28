lista = []

for i in range(10):
    val = int(input('Digite {} valores: '.format(i+1)))
    lista.append(val)

print(' ')

m = int(input('Digite um valor qualquer: '))

print(' ')

if m in lista:
    print('a posição em que "m" ocupa na lista é: {}'.format(lista.index(m)))
else:
    print('O valor "m" não está contido nesta lista')