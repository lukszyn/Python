#Zadanie 2
#Napisz skrypt, który obliczy pierwiastki równania kwadratowego.

import math

NAZWA2="Zadanie 2"
print("program",NAZWA2)
print('****************')

print("Podaj wspolczynniki rownania kwadatowego ax^2 + bx + c = 0")
print("Podaj a: ",end="")
a=input()
print("Podaj b: ",end="")
b=input()
print("Podaj c: ",end="")
c=input()

delta=int(b)**2-(4*int(a)*int(c))

if delta<0:
    print("Brak rozwiazan rownania dla liczb rzeczywistych.")

elif delta==0:
    x=(-int(b))/(2*int(a))
    print("x = ",round(x,2))

else:
    x1=(-int(b)+math.sqrt(delta))/(2*int(a))
    x2=(-int(b)-math.sqrt(delta))/(2*int(a))
    print("x1 = ",round(x1,2))
    print("x2 = ",round(x2,2))