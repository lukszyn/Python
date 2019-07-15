try:
    import m1
except ImportError:
    print('Blad importu')
    raise SystemExit
lista=[]
print('Podaj dlugosci bokow: ')
print('Podaj dlugosc boku a:',end='')
lista.append(int(input()))
print('Podaj dlugosc boku b:',end='')
lista.append(int(input()))
print('Podaj dlugosc boku c:',end='')
lista.append(int(input()))
print(lista)
m1.nierownoscTrojkata(lista)
