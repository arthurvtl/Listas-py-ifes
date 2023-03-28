import random

lista = []


for i in range(50):
    nums = random.randrange(0,50)
    lista.append(nums)

vm = max(lista)
pos = lista.index(vm)

print(' ')
print(lista)
print(' ')
print('O maior número da lista é: ' , vm)
print('A posição do maior número é: ' , pos)