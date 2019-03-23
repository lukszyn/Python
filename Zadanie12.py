#ZADANIE 12
#Napisz skrypt, którego zadaniem będzie wyświetlenie macierzy
#transponowanej (zamiana wierszy w kolumny) na podstawie macierzy
#umieszczonej poniżej.

lista=[[1,1,1],[1,1,1],[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,5):
    for j in range(0,3):
        print(lista[i][j],end=' ')
    print()
print()
for i in range(0,3):
    for j in range(0,5):
        print(lista[j][i],end=' ')
    print()