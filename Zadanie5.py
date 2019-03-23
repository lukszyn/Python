#Zad.5
#Napisz skrypt, który:
    #wprowadzi ciąg liczb, którego znacznikiem końca jest liczba 100.
    #Liczba 100 może, ale nie musi być zapisywana do zbioru.
    #wyświetl tylko te elementy ciągu, których wartości są mniejsze od 25.

NAZWA1="Zadanie 5"
print("program",NAZWA5)
print('****************')
lista=[]
i=0

while i!=100:
    print('Wprowadz liczbe nr',i+1,": ",end='')
    e=int(input())
    lista.append(e)
    if e==100: break
    i+=1
print('Elementy listy mniejsze od 25: ')

for i in lista:
    if i<25:
        print(i, end=', ')