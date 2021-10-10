# -*- coding: utf-8 -*-
"""
Created on sun Oct 10 10:45:35 2021

@author: lulualfina15
"""

import math

a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

print(f"Persamaan kuadrat {a}x^2 + {b}x + {c}")

if a==0:
   print("tidak valid nilai a, tidak boleh sama dengan 0")    

else:
    D = (b**2) - (4*a*c)
    print("determinan", D)
    
    if (D<0):
       print("akar imaginer")

    elif (D==0):
       x = ("-b + math.sqrt (D)) / (2*a)")
       print("x1=x2")
    
    else:
       x1 = (-b + math.sqrt(D)) / (2*a)
       x2 = (-b - math.sqrt(D)) / (2*a)
       print("x1 = x1")
       print("x2 = x2")
