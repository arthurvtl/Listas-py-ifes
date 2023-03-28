lista_notas = []
lista_matriculas = []
cont = 0
cont2 = 0



for i in range(5):
    notas = float(input('Digite o valor de 5 notas: '))
    lista_notas.append(notas)

    matriculas = str(input('Digite sua matrícula: '))
    lista_matriculas.append(matriculas)

soma_notas = sum(lista_notas)
media_notas = soma_notas/len(lista_notas)

for i in range (len(lista_notas)):
    if lista_notas[i] > media_notas:
        cont += 1
    else:
        cont2 += 1

print('A média é de: {}'.format(media_notas))
print(' ')
print('A quantidade de notas acima da média é de: {}'.format(cont))
print(' ')
print('A quantidade de notas abaixo da média é de: {}'.format(cont2))
        
    
    
    
