# ZADANIE 13
#Napisz skrypt, który utworzy zbiór liczb N ={0,1,2,3…} w postaci listy.
#Wielkość zbioru podaje użytkownik.
#Ponadto oczekiwania wobec skryptu są następujące:
    #wyświetlić i obliczyć sumę wszystkich elementów tablicy, których
    #indeks jest liczbą parzystą,
    #wyświetlić i obliczyć sumę wszystkich elementów tablicy, których
    #indeks jest liczbą nieparzystą,
    #sprawdzić zależność (<,>,=) między w/w sumami.

print("Podaj wielkosc zbioru liczb naturalnych N: ",end='')
n = int(input())
lista = []
sumaParzystych = 0
sumaNieparzystych = 0

for i in range(n):
    print("Podaj {} wyraz ciagu: ".format(i+1),end='')
    lista.append(int(input()))

print('\nPodana lista: ',lista)

for i in range(0, n, 2):
    sumaParzystych = sumaParzystych + lista[i]

print("Suma elementów o parzystych indeksach wynosi: ", sumaParzystych)

for i in range(1, n, 2):
    sumaNieparzystych = sumaNieparzystych + lista[i]

print("Suma elementów o nieparzystych indeksach wynosi: ", sumaNieparzystych)

if sumaParzystych > sumaNieparzystych:
    print("Suma elementow o parzystych indeksach listy jest wieksza.")

elif sumaParzystych < sumaNieparzystych:
    print("Suma elementow o nieparzystych indeksach listy jest wieksza.")

else:
    print("Sumy sa rowne.")