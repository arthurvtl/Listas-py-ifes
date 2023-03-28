import random

lista = []


for i in range (12):
    val = random.randrange(0,12)
    lista.append(val)

x = int(input('Digite um valor para x (digite um valor entre 0 e 11): '))
y = int(input('Digite um valor para y (digite um valor entre 0 e 11): '))

conta = lista[x] + lista[y]

print(lista.index(x))
print(lista.index(y))
print(conta)
