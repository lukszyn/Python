# ZADANIE 14
#Napisz skrypt, który utworzy zbiór liczb N ={0,1,2,3…}) w postaci listy.
#Wielkość zbioru podaje użytkownik. Napisz skrypt, który wykona
#potęgowanie liczb należących do w/w zbioru. Wykładnikiem potęgi
#jest indeks elementu.
#Ponadto oczekiwania wobec skryptu są następujące:
    #wykonać potęgowanie wszystkich elementów zbioru, których
    #indeks jest nieparzysty i obliczyć oraz wyświetlić sumę po
    #potęgowaniu,
    #wykonać potęgowanie wszystkich elementów tablicy, których
    #indeks jest parzysty i obliczyć i wyświetlić sumę po potęgowaniu,
    #sprawdzić zależność (<,>,=) między w/w sumami.
    
print("Podaj wielkosc zbioru liczb naturalnych N: ")
n = int(input())
lista = []
sumaNieparzystych = 0
sumaParzystych = 0

for i in range(n):
    print("Podaj {} wyraz ciagu: ".format(i+1),end='')
    lista.append(int(input()))

for i in range(n):
    if i%2!=0:
        lista[i] = lista[i] ** i
        sumaNieparzystych = sumaNieparzystych + lista[i]
    else:
        lista[i] = lista[i] ** i
        sumaParzystych = sumaParzystych + lista[i]

print()
print('Spotegowana lista: ',end='')
print(lista)
print("Suma spotegowanych elementów o nieparzystych indeksach wynosi: ", sumaNieparzystych)
print("Suma spotegowanych elementów o parzystych indeksach wynosi: ", sumaParzystych)

if sumaParzystych > sumaNieparzystych:
    print("Suma elementow o parzystych indeksach listy jest wieksza.")

elif sumaParzystych < sumaNieparzystych:
    print("Suma elementow o nieparzystych indeksach listy jest wieksza.")

else:
    print("Sumy sa rowne.")