#ZADANIE 9
#Napisz skrypt, który pozwoli użytkownikowi na wprowadzenie i
#zapisanie dziesięciu liczb naturalnych N={1,2,3,..} do listy.
#Ponadto zadaniem skryptu jest spotęgowanie wszystkich elementów
#listy w oparciu o funkcję „potęga” z argumentem funkcji w postaci
#wykładnika potęgi. Funkcja musi zwracać wynik w postaci listy zawierającej spotęgowane elementy.

def potega(n):
    for i in range(len(lista)):
        lista[i]=lista[i]**n
    return lista

lista=[]

print('Podaj 10 elementow listy:')

for i in range (0,3):
    a=int(input())
    lista.append(a)

print(lista)
print('Podaj liczbe do potegi ktorej chcesz podniesc elementy listy: ',end='')
n=int(input())
potega(n)
print('Elementy listy podniesione do potegi ',n,': ')
print(lista)


