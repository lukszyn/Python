import time

def zapisz(rejestr):

    imie = str(input("Podaj swoje imię: "))
    rejestr.write(imie)
    data = time.strftime(" - %Y-%m-%d - %H:%M\n", )
    rejestr.write(data)


def wyswietl(rejestr):
    rejestr.seek(0)
    zawartosc_rejestru = rejestr.read()
    print(zawartosc_rejestru)


def zamknij(rejestr):
    rejestr.close()
    raise SystemExit