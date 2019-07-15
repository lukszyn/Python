# -*- coding: ISO-8859-2 -*-
import os
import m33

def menu():

    plik = str(input("Podaj nazw� pliku: "))

    if os.path.isfile(plik):
        rejestr = open(plik, 'a+')
        print("Otwarto plik: {}".format(rejestr.name))
    else:
        rejestr = open(plik, 'a+')
        print("Utworzono plik: {}".format(rejestr.name))

    while True:
        wybor = int(input("Wybierz opcj� programu:\n"
                          "1 - Wy�wietl rejestr\n"
                          "2 - Zapisz do rejestru\n"
                          "3 - Wyj�cie\n"
                          "Opcja: "))

        if wybor == 1:
            m33.wyswietl(rejestr)
        elif wybor == 2:
            m33.zapisz(rejestr)
        elif wybor == 3:
            m33.zamknij(rejestr)
        else:
            print("Nie ma takiej opcji!")
            continue

menu()