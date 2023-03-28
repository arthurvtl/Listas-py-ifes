lista = []
listaNova = []

for i in range (20):
    lista.append(i)
    listaNova.append(i)

listaNova.reverse()

print('A lista original é: \n {}'.format(lista))
print(' ')
print('A lista espelhada é: \n {}'.format(listaNova))