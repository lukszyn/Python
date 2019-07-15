# -*- coding: ISO-8859-2 -*-

import datetime

class Osoba():


    def __init__(self, imie, nazwisko, rok_urodzenia):

        self.imie = imie
        self.nazwisko = nazwisko
        self.rok_urodzenia = rok_urodzenia


    def __gt__(self, other):
        return self.rok_urodzenia > other.rok_urodzenia


    def okreslWiek(self):

        data = datetime.datetime.now()
        obecny_rok = data.year
        wiek = obecny_rok - self.rok_urodzenia
        return wiek


    def czyDojrzala(self):

        wiek = Osoba.okreslWiek(self)

        if wiek <= 30:
            czy_dojrzala = 'osoba młoda'
        elif wiek <= 60:
            czy_dojrzala = 'osoba dojrzała'
        else:
            czy_dojrzala = 'osoba starsza'

        return czy_dojrzala


    def zapisz(self):

        plik.seek(0)
        ile = len(plik.readlines())
        wiek = Osoba.okreslWiek(self)
        czy_dojrzala = Osoba.czyDojrzala(self)

        plik.write("{}. ".format(ile + 1))
        plik.write(self.imie)
        plik.write(" {} - ".format(self.nazwisko))
        plik.write("wiek: {} - {}\n".format(wiek, czy_dojrzala))

with open('osoby.txt', 'w+') as plik:

    imie1 = input("Podaj imię pierwszej osoby: ")
    nazwisko1 = input("Podaj nazwisko pierwszej osoby: ")
    rok1 = int(input("Podaj rok urodzenia pierwszej osoby: "))
    osoba1 = Osoba(imie1, nazwisko1, rok1)
    Osoba.zapisz(osoba1)

    imie2 = input("Podaj imię drugiej osoby: ")
    nazwisko2 = input("Podaj nazwisko drugiej osoby: ")
    rok2 = int(input("Podaj rok urodzenia drugiej osoby: "))
    osoba2 = Osoba(imie2, nazwisko2, rok2)
    Osoba.zapisz(osoba2)

    imie3 = input("Podaj imię trzeciej osoby: ")
    nazwisko3 = input("Podaj nazwisko trzeciej osoby: ")
    rok3 = int(input("Podaj rok urodzenia trzeciej osoby: "))
    osoba3 = Osoba(imie3, nazwisko3, rok3)
    Osoba.zapisz(osoba3)

    if (osoba1.__gt__(osoba2)) and (osoba1.__gt__(osoba3)):
        plik.write("Osoba najmłodsza: {} {}\n".format(osoba1.imie, osoba1.nazwisko))
    elif (osoba2.__gt__(osoba1)) and (osoba2.__gt__(osoba3)):
        plik.write("Osoba najmłodsza: {} {}\n".format(osoba2.imie, osoba2.nazwisko))
    elif (osoba3.__gt__(osoba1)) and (osoba3.__gt__(osoba2)):
        plik.write("Osoba najmłodsza: {} {}\n".format(osoba3.imie, osoba3.nazwisko))

    plik.seek(0)
    zawartosc_pliku = plik.read()
    print(zawartosc_pliku)
    plik.close()