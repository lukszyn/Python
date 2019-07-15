# ZADANIE 30

import math

class Punkt3D:

    def __init__(self, wspolrzedne):
        self.wspolrzedne = wspolrzedne

    def przesuniecie(self):
        przesuniecie = []
        print("Podaj wektor przesuniecia punktu:")
        przesuniecie.append(float(input("Wspolrzedna x: ")))
        przesuniecie.append(float(input("Wspolrzedna y: ")))
        przesuniecie.append(float(input("Wspolrzedna z: ")))
        for i in range(len(self.wspolrzedne)):
            self.wspolrzedne[i] += przesuniecie[i]
        print("Wspolrzedne punktu przesunietego o wektor {} wynosza: {}\n".format(przesuniecie,self.wspolrzedne))

    def obrot(self):
        os = input("Wybierz os obrotu (x, y lub z): ")
        kat = float(input("Podaj kat obrotu: "))

        if os == 'x':
            Rx = [[1,0,0],[0,math.cos(kat),-math.cos(kat)],[0,math.sin(kat),math.cos(kat)]]
            macierzWspolrz = [[wspolrzedne[0]],[wspolrzedne[1]],[wspolrzedne[2]]]
            wynik = [[0],[0],[0]]

            for i in range(len(Rx)):
                for j in range(len(macierzWspolrz[0])):
                    for k in range(len(macierzWspolrz)):
                        wynik[i][j] += Rx[i][k] * macierzWspolrz[k][j]
            print("Wspolrzedne obroconego punktu: [{:.2f}, {:.2f}, {:.2f}]\n".format(wynik[0][0],wynik[1][0],wynik[2][0]))

        elif os == 'y':
            Ry = [[math.cos(kat), 0, math.sin(kat)], [0,1,0],[-math.sin(kat),0,math.cos(kat)]]
            macierzWspolrz = [[wspolrzedne[0]], [wspolrzedne[1]], [wspolrzedne[2]]]
            wynik = [[0], [0], [0]]

            for i in range(len(Ry)):
                for j in range(len(macierzWspolrz[0])):
                    for k in range(len(macierzWspolrz)):
                        wynik[i][j] += Ry[i][k] * macierzWspolrz[k][j]
            print("Wspolrzedne obroconego punktu: [{:.2f}, {:.2f}, {:.2f}]\n".format(wynik[0][0], wynik[1][0], wynik[2][0]))

        elif os == 'z':
            Rz = [[math.cos(kat), -math.sin(kat), 0], [math.sin(kat), math.cos(kat), 0],[0, 1, 0]]
            macierzWspolrz = [[wspolrzedne[0]], [wspolrzedne[1]], [wspolrzedne[2]]]
            wynik = [[0], [0], [0]]
            for i in range(len(Rz)):
                for j in range(len(macierzWspolrz[0])):
                    for k in range(len(macierzWspolrz)):
                        wynik[i][j] += Rz[i][k] * macierzWspolrz[k][j]
            print("Wspolrzedne obroconego punktu: [{:.2f}, {:.2f}, {:.2f}]\n".format(wynik[0][0], wynik[1][0], wynik[2][0]))

        else:
            print("Podano błędną os.")

    def rzutowanie(self):

        print("Podaj wspolrzedne plaszczyzny Ax + By + Cz + D = 0")
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        d = float(input("D: "))

        t = -(wspolrzedne[0]*a+wspolrzedne[1]*b+wspolrzedne[2]*c+d)/(a**2+b**2+c**2)
        x = wspolrzedne[0]+a*t
        y = wspolrzedne[1]+b*t
        z = wspolrzedne[2]+c*t
        print("Wspolrzedne zrzutowanego punktu: [{:.2f}, {:.2f}, {:.2f}]\n".format(x,y,z))

def menu(wspolrzedne):
    wybor = 1
    punkt = Punkt3D(wspolrzedne)
    while wybor!=0:
        wybor = int(input("Wybierz opcje programu:\n"
                          "1 - Przesuniecie punktu\n"
                          "2 - Obrot punktu\n"
                          "3 - Rzutowanie  punktu na plaszczyzne\n"
                          "0 - Zakoncz\n"))
        if wybor == 1:
            punkt.przesuniecie()
        elif wybor == 2:
            punkt.obrot()
        elif wybor == 3:
            punkt.rzutowanie()
        elif wybor == 0:
            break
        else:
            print("Nie ma takiej opcji!")

def podajWspolrzedne():
        wspolrzedne = []
        print("Podaj wspolrzedne punktu:")
        wspolrzedne.append(float(input("Wspolrzedna x: ")))
        wspolrzedne.append(float(input("Wspolrzedna y: ")))
        wspolrzedne.append(float(input("Wspolrzedna z: ")))
        print("Wspolrzedne wynosza: {}".format(wspolrzedne))
        print()
        return wspolrzedne

wspolrzedne = podajWspolrzedne()
menu(wspolrzedne)
