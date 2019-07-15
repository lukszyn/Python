#ZADANIE 30

# -*- coding: ISO-8859-2 -*-
import os

def menu():

    plik = str(input("Podaj nazwê pliku: "))

    if os.path.isfile(plik):
        rejestr = open(plik, 'a+')
        print("Otwarto plik: {}".format(rejestr.name))
    else:
        print("Podany plik nie istnieje.")
        raise SystemExit

    wybor = 1
    while wybor != 0:
        wybor = int(input("\nWybierz opcjê programu:\n"
                          "1 - Wy¶wietl rejestr\n"
                          "2 - Zapisz do rejestru\n"
                          "3 - Wyj¶cie\n"
                          "Opcja: "))

        if wybor == 1:
            rejestr.seek(0)
            zawartosc_rejestru = rejestr.read()
            print(zawartosc_rejestru)
        elif wybor == 2:
            imie = str(input("Podaj swoje imiê: "))
            rejestr.write(imie)
            data = time.strftime(" - %Y-%m-%d - %H:%M\n", )
            rejestr.write(data)
        elif wybor == 3:
            rejestr.close()
            raise SystemExit
        else:
            print("Nie ma takiej opcji!")
            continue

menu()