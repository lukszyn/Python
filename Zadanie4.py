# Zadanie 4
#Napisz skrypt, który:
    #utworzy listę jednowymiarową, składającą się z 10 liczb
    #naturalnych N={0, 1, 2, …}
    #znajdzie i wyświetli wartość maksymalną spośród wszystkich
    #elementów listy
    #obliczy sumę wszystkich elementów parzystych listy

NAZWA4="Zadanie 4"
print("program",NAZWA4)
print('****************')
lista=[]
i=0
suma=0
max=0
for i in range (0,4):
    print('Podaj ',i+1,' liczbe: ',end='')
    e=int(input())
    lista.append(e)
    if e>max: max=e
    if e%2==0: suma=suma+e
print('Wpisana lista: ',lista)
print('Najwiekszy element listy wynosi: ',max)
print('Suma elementow parzystych listy wynosi: ',suma)