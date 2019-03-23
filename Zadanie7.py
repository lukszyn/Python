# ZADANIE 7

lista1 = [[1, 2, 3], [1, 2, 0], [1, 0, 2]]
lista2 = [[5], [5], [5]]

for i in range(len(lista1)):
    for j in range(len(lista1[i])):
        print(lista1[i][j], end=' ')
    print()

print('\n')
suma = 0

for i in range(len(lista1)):
    for j in range(len(lista1[i])):
        if i == j:
            lista1[i][j] = lista2[i][0]
            suma = suma + lista2[i][0]

for i in range(len(lista1)):
    for j in range(len(lista1[i])):
        print(lista1[i][j], end=' ')
    print()

print('Suma elementow po przekatnej wynosi: ', suma)