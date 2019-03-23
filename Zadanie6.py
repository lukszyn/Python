#Zadanie 6
#Napisz skrypt, który pozwoli użytkownikowi na wprowadzenie i
    #zapisanie dziesięciu liczb naturalnych N={1,2,3,..} do listy.
    #Ponadto zadaniem skryptu jest obliczenie i wyświetlenie sumy tylko
    #tych liczb, które są parzyste i większe od 10.
    #Skrypt musi wyświetlić również ilość zsumowanych elementów.

lista=[]
print('Podaj 10 elementow listy:')
for i in range (0,10):
    a=int(input())
    lista.append(a)

suma=0
ile=0
for i in lista:
    if i>10 and i%2==0:
        suma=suma+i
        ile=ile+1
print('Suma wynosi: ',suma)
print('Ilosc sumowanych elementow: ',ile)