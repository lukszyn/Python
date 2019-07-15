# ZADANIE 29


class Automat:

    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    def pokaz_cene(self):
        print("Wybrano napoj: {}, cena: {:.2f} zl".format(self.nazwa, self.cena))

    def wydaj_reszte(self):
        kwota = float(input("Podaj kwote wrzucona do automatu: "))
        if kwota >= self.cena:
            reszta = kwota - self.cena
            print("Reszta: {:.2f} zl\n".format(reszta))
        else:
            print("Brakuje {} zl".format(self.cena - kwota))


def menu():
    wybor = 1
    while wybor != 0:
        wybor = int(input("Wybierz napoj:\n"
                          "1 - Coca Cola,\n"
                          "2 - Pepsi\n"
                          "3 - Sprite\n"
                          "4 - Fanta\n"
                          "0 - Zakoncz\n"))
        if wybor == 1:
            napoj1.pokaz_cene()
            napoj1.wydaj_reszte()
        elif wybor == 2:
            napoj2.pokaz_cene()
            napoj2.wydaj_reszte()
        elif wybor == 3:
            napoj3.pokaz_cene()
            napoj3.wydaj_reszte()
        elif wybor == 4:
            napoj4.pokaz_cene()
            napoj4.wydaj_reszte()
        else:
            print("Nie ma takiej opcji!")
            break


napoj1 = Automat('Coca Cola', 2.50)
napoj2 = Automat('Pepsi', 3.00)
napoj3 = Automat('Sprite', 2.70)
napoj4 = Automat('Fanta', 2.00)
menu()
