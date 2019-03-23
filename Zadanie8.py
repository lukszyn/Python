#ZADANIE 8
#Napisz skrypt, który pozwoli użytkownikowi na wprowadzenie i
#zapisanie dziesięciu liczb naturalnych N={1,2,3,..} do listy.
#Ponadto zadaniem skryptu jest obliczenie i wyświetlenie wartości
#maksymalnej.

lista=[]
i=0
suma=0
max=0

for i in range(0,10):
    print('Podaj ',i+1,' liczbe: ',end='')
    e=int(input())
    lista.append(e)
    if e>max: max=e

print('Wpisana lista: ',lista)
print('Najwiekszy element listy wynosi: ',max)
