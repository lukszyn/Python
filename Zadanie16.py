#ZADANIE 16
#Napisz skrypt, którego zadaniem będzie rozwiązanie układu dwóch równań.

print("Podaj wspolczynniki w ukladzie rownan w postaci:\n\t a1*x + b1*y = c1\n\t a2*x + b2*y = c2")
symbole=[['a1','a2'],['b1','b2'],['c1','c2']]
lista=[]

for i in range(0,3):
    lista.append([])
    for j in range(0,2):
        print("Podaj wspolczynnik",symbole[i][j],": ")
        lista[i].append(float(input()))

W=lista[0][0]*lista[1][1]-lista[1][0]*lista[0][1]
Wx=lista[2][0]*lista[1][1]-lista[1][0]*lista[2][1]
Wy=lista[0][0]*lista[2][1]-lista[2][0]*lista[0][1]

if W:
    print("x =",Wx/W)
    print("y=",Wy/W)
elif W==0 and Wx==0 and Wy==0:
    print("Uklad ma nieskonczenie wiele rozwiazan.")
else:
    print("Uklad sprzeczny.")