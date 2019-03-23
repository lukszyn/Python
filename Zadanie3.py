#Zadanie 3
#Napisz skrypt, który:
    #wczyta dwie wartości dodatnie (N={0, 1, 2, …}), parzyste oraz
    #należące do przedziału <10;100>
    #obliczy i wyświetli sumę podanych liczb

NAZWA3="Zadanie 3"
print("program",NAZWA3)
print('****************')

print("Podaj dodatnie liczby a i b.")
print("Podaj a: ",end="")

a=input()
if int(a)<=0:
    print("Liczba a jest niedodatnia!")
elif int(a)%2!=0:
    print("Liczba a jest nieparzysta!")
elif int(a)<10:
    print("Liczba a jest mniejsza od 10!")
elif int(a)>100:
    print("Liczba a jest wieksza od 100!")
print("Podaj b: ",end="")

b=input()
if int(b)<=0:
    print("Liczba b jest niedodatnia!")
elif int(b)%2!=0:
    print("Liczba b jest nieparzysta!")
elif int(b)<10:
    print("Liczba b jest mniejsza od 10!")
elif int(b)>100:
    print("Liczba b jest wieksza od 100!")

if  int(a)>=10 and int(a)%2==0 and int(a)<=100 and int(b)>=10 and int(b)%2==0 and int(b)<=100:
    c=int(a)+int(b)
    print("Suma: ",a," + ",b," = ",c)
else:
    print("Podano niepoprawne liczby.")'''

