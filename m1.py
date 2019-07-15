def nierownoscTrojkata(lista):
    lista.sort()
    if lista[0]<lista[1]+lista[2] and lista[1]<lista[0]+lista[2] and lista[2]<lista[0]+lista[1]:
        print("Podane wartosci moga byc bokami trojkata")
    else: print("Podane boki nie stworza trojkata")
    return None

def czyProstokatny(a,b,c):
        x=lambda y,z: y**2+z**2
        d=x(a,b)
        if d==c**2:
            print("Trojkat o podanych dlugosciach jest prostokatny.")
        else:
                print("Trojkat o podanych dlugosciach nie jest prostokatny.")

def generowanieCiagu(a,b):
    import random
    lista=[]
    for i in range(a,b+1,2):
        if i==a:
            lista.append(a)
        elif i==b:
            lista.append(b)
        else:
            lista.append(i)
    print('Wygenerowano liste: ',lista)
    random.shuffle(lista)
    print('Losowo posortowana lista ma postac: ', lista)
    
def zestawCyfr(a):
    for i in range(a):
        for j in range(i+1):
            print(i+1,end='   ')
        print()

def piramida(a):
    for i in range(1,a):
        for j in range(1,4*(a-i)):
            print(" ",end='')
        for k in range (0,(2*i-1)):
            print('* ',end='')
        print()
