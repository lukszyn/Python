#ZADANIE 10
#Napisz skrypt, który:
    #utworzy listę o rozmiarze 3×3, której każe pole wypełni cyfrą 1
    #wyświetli w/w tablicę w układzie 3×3
    #poprosi o podanie jednej liczby naturalnej N={1,2,3,..}
    #wstawi w/w liczbę w tablicy w polu [1][1]
    #wyświetli w/w tablicę w układzie 3×3 po zmianach

lista=[[1,1,1],[1,1,1],[1,1,1]]
for i in range(0,3):
    for j in range(0,3):
        print(lista[i][j],end=' ')
    print()
print('\n')

print('Podaj liczbe naturalna: ',end='')
e=int(input())
lista[1][1]=e

for i in range(0,3):
    for j in range(0,3):
        print(lista[i][j],end=' ')
    print()

print('\n')


