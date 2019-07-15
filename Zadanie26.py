#ZADANIE 26

try:
    import m1
except ImportError:
    print('Blad importu')
    raise SystemExit

print("Podaj liczbe naturalna: ",end=' ')
a=int(input())
m1.piramida(a)
