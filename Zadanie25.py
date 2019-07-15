#ZADANIE 25

try:
    import m1
except ImportError:
    print('Blad importu')
    raise SystemExit

print("Podaj dowolna liczbe naturalna: ",end=' ')
a=int(input())
m1.zestawCyfr(a)
