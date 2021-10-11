@author: lulualfina15
"""

from math import sqrt

a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

D = (b**2) - (4*a*c)

if a == 0:
    print("A tidak boleh sama dengan 0")
else:
    print(f"Persamaan Kuadrat {a}x^2 + {b}x + {c}")
    print(f"Determinan = {D}")

    if (D<0):
        print("Akar Imaginer")
        print(f"x1 = -b + Akar {D} / 2*a")
        print(f"x2 = -b - Akar {D} / 2*a")
    elif (D==0):
        x1 = -b / (2*a)
        x2 = x1
        print("Akar Kembar")
        print(f"Akar x1 = {x1}")
        print(f"Akar x2 = {x2}")
    elif (D>0):
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        print("Akar Berbeda")
        print(f"Akar x1 = {x1}")
        print(f"Akar x2 = {x2}")
