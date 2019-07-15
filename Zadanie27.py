# ZADANIE 27

def menu():

    while True:
        print('***** MENU *****')
        print('1 - Wprowadz dane o nowym pojezdzie')
        print('2 - Wyswietl dane o pojezdzie')
        print('3 - Usun dane o pojezdzie')
        print('x - Wyjdz z programu')
        wybor = input('Wybierz opcje programu: ')
        if wybor == '1':
            ob = Pojazd()
            ob.dodajPojazd()
        elif wybor == '2':
            ob.pokazDane()
        elif wybor == '3':
            del ob
        elif wybor == 'x':
            break
        else:
            print('Niewlasciwa opcja')


class Pojazd:

    def dodajPojazd(self):
        self.marka = input('Podaj marke samochodu: ')
        self.model = input('Podaj model samochodu: ')
        self.rokProd = int(input('Podaj rok produkcji samochodu: '))

    def pokazDane(self):
        print('Marka: ', self.marka)
        print('Model: ', self.model)
        print('Rok produkcji: ', self.rokProd)


menu()