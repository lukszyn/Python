# ZADANIE 28

def menu():

    while True:
        print('***** MENU *****')
        print('1 - Wprowadz dane o nowym pojezdzie')
        print('2 - Wyswietl dane o pojezdzie')
        print('3 - Usun dane o pojezdzie')
        print('x - Wyjdz z programu')
        wybor = input('Wybierz opcje programu: ')

        if wybor == '1':
            print("\nWybierz typ pojazdu:\n"
                  "o - samochod osobowy\n"
                  "m - motocykl")
            typ = input("Typ: ")
            if typ == 'o':
                ob = Osobowy("samochod osobowy")
            elif typ == 'm':
                ob = Motocykl("motocykl\n")

        elif wybor == '2':
            try:
                ob.pokazDane()
            except:
                print("Nie wprowadzono zadnego pojazdu!\n")
                continue

        elif wybor == '3':
            try:
                del ob
                print("Usunieto pojazd.")
            except:
                print("Nie wprowadzono zadnego pojazdu!\n")
                continue
        elif wybor == 'x':
            break
        else:
            print('Niewlasciwa opcja')


class Pojazd:

    def dodajPojazd(self):
        self.marka = input('Podaj marke pojazdu: ')
        self.model = input('Podaj model pojazdu: ')
        self.rokProd = int(input('Podaj rok produkcji pojazdu: '))

    def pokazDane(self):
        print('\nMarka: {}'.format(self.marka))
        print('Model: {}'.format(self.model))
        print('Rok produkcji: {}'.format(self.rokProd))

class Osobowy(Pojazd):

    def __init__(self, typ):
        Pojazd.dodajPojazd(self)
        self.typ = typ

    def pokazDane(self):
        Pojazd.pokazDane(self)
        print("Typ pojazdu: {}\n".format(self.typ))

class Motocykl(Pojazd):

    def __init__(self, typ):
        Pojazd.dodajPojazd(self)
        self.typ = typ

    def pokazDane(self):
        Pojazd.pokazDane(self)
        print("Typ pojazdu: {}".format(self.typ))
menu()