#ZADANIE 23
#Napisz skrypt, który:
    #poprosi użytkownika o wprowadzenie 10 wartości należących do
    #zbioru N={0,1,2,…}
    #w/w wartości zapisze do listy
    #wyświetli wszystkie elementy w/w listy
    #losowo posortuje elementy listy
    #losowo wybierze z listy 3 elementy
    #wyświetli w/w elementy po spotęgowaniu (wykładnik potęgi = 3)

import random

lista=[]

print('Podaj 10 liczb naturalnych.')

for i in range(0, 10):
    print('Podaj {} element:'.format(i+1),end=' ')
    lista.append(int(input()))
print("Podana lista ma postac: {}".format(lista))

i=random.shuffle(lista)
print(lista)

i=random.sample(lista,3)
print(i)

for i in range(len(lista)):
    lista[i]=lista[i]**3

i=random.shuffle(lista)
print(lista)

i=random.sample(lista,3)
print(i)
