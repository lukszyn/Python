#ZADANIE 24
try:
    import m1
except ImportError:
    print('Blad importu')
    raise SystemExit
from random import shuffle
print('Podaj wartosci poczatkowa i koncowa ciagu: ')
print('Podaj wartosc poczatkowa:',end=' ')
a=int(input())
print('Podaj wartosc koncowa:',end=' ')
b=int(input())

m1.generowanieCiagu(a,b)
