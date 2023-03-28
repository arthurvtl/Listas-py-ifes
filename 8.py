lista = []

for i in range(10):
    idades = int(input('Digite {} idades: '.format(i-1)))
    lista.append(idades)

soma_i = sum(idades)
media_i = soma_i / len(lista)

