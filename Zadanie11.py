# ZADANIE 11
#Napisz skrypt, który:
    #wczytuje macierz kwadratową liczb naturalnych (N={0,1,2,3…})
    #wymiaru „n” (elementy macierzy oraz „n” podaje użytkownik z
    #klawiatury)
    #wypisuje elementy macierzy na ekranie monitora
    #oblicza iloczyn tych elementów tej macierzy, które są podzielne
    #przez 3 lub 4 i wypisuje obliczony iloczyn na ekranie

lista = []
print('Podaj liczbe naturalna: ', end='')
n = int(input())

for i in range(0, n):
    lista.append([])
    for j in range(0, n):
        print('Podaj element [', i + 1, '][', j + 1, '] macierzy')
        lista[i].append(int(input()))

for i in range(0, n):
    for j in range(0, n):
        print(lista[i][j], end=' ')
    print()

iloczyn = 1

for i in range(0, n):
    for j in range(0, n):
        if lista[i][j] % 4 == 0 or lista[i][j] % 3 == 0:
            iloczyn = iloczyn * lista[i][j]

print('Iloczyn elementow podzielnych przez 3 i 4 wynosi: ', iloczyn)

