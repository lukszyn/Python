try:
    import m2
except ImportError:
    print('Blad importu')
    raise SystemExit
import random as r

lista=[]
for i in range(10):
    lista.append(r.randint(1,1000))

print('Wylosowano dlugosci bokow trojkata:',end='')
print(lista)
m2.czyTrojkat(lista)
