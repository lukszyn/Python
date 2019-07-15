# -*- coding: utf-8 -*-
import re

nazwa = ['nazwisko', 'PESEL', 'data urodzenia', 'numer telefonu', 'miasto', 'kod pocztowy']
dane = []
szablon = []

nazwisko = input("Podaj nazwisko: ")
dane.append(nazwisko)
szablon.append('^([A-Z,ŁŻĆŚŹ])([a-z,ąężźśćńół]{2,})$')

pesel = input("Podaj PESEL: ")
dane.append(pesel)
szablon.append('[0-9]{11}')

data_urodzenia = input("Podaj date urodzenia: ")
dane.append(data_urodzenia)
szablon.append('^(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-1][0-9])$')

nr_tel = input("Podaj numer telefonu: ")
dane.append(nr_tel)
szablon.append('^\+48\s\d\d\d\-\d\d\d\-\d\d\d$')

miasto = input("Podaj miasto zamieszkania: ")
dane.append(miasto)
szablon.append('^([A-Z,ŁŻĆŚŹ])([a-z,ąężźśćńół]{2,})$')

kod_pocztowy = input("Podaj kod pocztowy: ")
dane.append(kod_pocztowy)
szablon.append('^(\d\d\-\d\d\d)$')

for element in range(len(dane)):

    try:
        dopasowanie = re.match(szablon[element], dane[element]).group()
        print("Wprowadzono pomyslnie: {}".format(nazwa[element]))
    except (TypeError, AttributeError):
        print("Podano niepoprawnie: {}".format(nazwa[element]))