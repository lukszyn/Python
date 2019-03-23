#ZADANIE 18
#Napisz skrypt wyświetlający tabliczkę mnożenia dla liczb od 1 do 100.

def tabliczkaMnozenia():

    for i in range(0, 11):
        for j in range(0, 11):
            k=i*j
            if k<10: print("{}".format(k),end='  ')
            else: print("{}".format(k),end=' ')
        print()

tabliczkaMnozenia()
