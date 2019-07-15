#ZADANIE 32

# -*- coding: ISO-8859-2 -*-

import os
import m32

def menu():

    plik = str(input("Podaj nazwę pliku: "))

    if os.path.isfile(plik):
        rejestr = open(plik, 'a+')
        print("Otwarto plik: {}".format(rejestr.name))
    else:
        print("Podany plik nie istnieje.")
        raise SystemExit

    wybor = 1
    while wybor != 0:
        wybor = int(input("Wybierz opcję programu:\n"
                          "1 - Wyświetl rejestr\n"
                          "2 - Zapisz do rejestru\n"
                          "3 - Wyjście\n"
                          "Opcja: "))

        if wybor == 1:
            m32.wyswietl(rejestr)
        elif wybor == 2:
            m32.zapisz(rejestr)
        elif wybor == 3:
            m32.zamknij(rejestr)
        else:
            print("Nie ma takiej opcji!")
            continue

menu()