#ZADANIE 17
#Napisz skrypt, którego zadaniem będzie sprawdzenie czy macierz B
#jest macierzą transponowaną w stosunku do macierzy A. Zakładamy,
#że rozmiar oby macierzy wynosi 4×4 oraz zakładamy, że elementami
#obu macierzy są liczby naturalne (N={0,1,2, …}), które wprowadza
#użytkownik.

macierzA = []
macierzB = []
macierzT = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print("Podaj macierz A romiarze 4x4")

for i in range(0, 4):
    macierzA.append([])
    for j in range(0, 4):
        print('Podaj element [', i + 1, '][', j + 1, '] macierzy')
        macierzA[i].append(int(input()))

print("Podana macierz ma postac:")

for i in range(0, 4):
    for j in range(0, 4):
        print(macierzA[i][j], end=' ')
    print()

print("Podaj macierz B romiarze 4x4")

for i in range(0, 4):
    macierzB.append([])
    for j in range(0, 4):
        print('Podaj element [', i + 1, '][', j + 1, '] macierzy')
        macierzB[i].append(int(input()))

print("Podana macierz B ma postac:")

for i in range(0, 4):
    for j in range(0, 4):
        print(macierzB[i][j], end=' ')
    print()

print("Macierz transponowana A ma postac:")

for i in range(0, 4):
    for j in range(0, 4):
        macierzT[i][j] = macierzA[j][i]
        print(macierzT[i][j], end=' ')
    print()

if macierzB == macierzT:
    print("Macierz B jest macierza transponowana do macierzy A")
else:
    print("Macierz B nie jest macierza transponowana do macierzy A")



