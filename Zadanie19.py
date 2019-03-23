#Zadanie 19
#Napisz skrypt, który w macierzy 10×10 umieści w pierwszej kolumnie
#liczby od 0 do 9, w drugiej kwadraty tych liczb, natomiast w
#pozostałych kolumnach 0 (zgodnie z poniższym wzorem).

macierz=[]

for i in range(0, 10):
    macierz.append([])
    for j in range(0, 10):
        if j < 2:
            macierz[i].append(i**(j+1))
            if macierz[i][j]<10:
                print("{}".format(macierz[i][j]), end='  ')
            else:
                print("{}".format(macierz[i][j]), end=' ')
        else:
            macierz[i].append(0)
            print("{}".format(macierz[i][j]), end=' ')
    print()