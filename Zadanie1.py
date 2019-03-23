#ZADANIE 1
## Napisz skrypt, który:
    ## wczyta dwie wartości należące do zbioru N={0, 1, 2, …}
    ## wyświetli wynik sumy w/w liczb
    ## wyświetli informację tylko w sytuacji, gdy suma liczb jest parzysta

NAZWA1="Zadanie 1"
print("program",NAZWA1)
print('****************')

print("Podaj liczbe naturalna a: ",end="")
a=input()

print("Podaj liczbe naturalna b: ",end="")
b=input()

print(a," + ",b," = ",end="")

c=int(a)+int(b)

print(c)

if c%2==0:
    print("Liczba ",c," jest parzysta.")