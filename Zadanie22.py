try:
    import m1
except ImportError:
    print('Blad importu')
    raise SystemExit

print('Podaj dlugosci bokow trojkata: ')
print('Podaj dlugosc boku a:',end='')
a=int(input())
print('Podaj dlugosc boku b:',end='')
b=int(input())
print('Podaj dlugosc boku c:',end='')
c=int(input())
m1.czyProstokatny(a,b,c)
