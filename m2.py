def czyTrojkat(lista):
    lista.sort()
    if lista[0]<lista[1]+lista[2] and lista[1]<lista[0]+lista[2] and lista[2]<lista[0]+lista[1]:
        print("Podane wartosci moga byc bokami trojkata")
    else: print("Podane boki nie stworza trojkata")
    return None
