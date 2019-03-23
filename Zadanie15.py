#ZADANIE 15
#Napisz i przetestuj funkcję z dwoma argumentami – wielkość zbioru
#liczb należąca do N ={1,2,3…} oraz wykładnik potęgi, należący
#również do N ={1,2,3…}. Zadaniem funkcji jest poproszenie
#użytkownika o wprowadzenie poszczególnych wartości zbioru z
#klawiatury oraz zwrócenie wyniku potęgowania.

def potegowanie(m,n):

    lista=[]
    for i in range(n):
        lista.append(i)
    for i in range(n):
        lista[i]=lista[i]**m
    return lista

print("Podaj wielkosc zbioru liczb naturalnych N: ")
n=int(input())
print("Podaj wykladnik potegi, nalezacy do zbioru liczb naturalnych: ")
m=int(input())
wynik=potegowanie(m,n)
print(wynik)
