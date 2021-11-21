@author: lulualfina15
"""

print("==========================")
print("    fungsi perpangkatan   ")
print("==========================")

def p(x,y):
    if y <= 1:
        return x
    else:
        return p(x,y-1) * p(x,1)
    
def n(x,y):
    b = abs(y)
    hasil = float(1/p(x,b))
    return hasil 

def hasil(x,y):      
    if y == 0:
        return 1
    elif x == 0:
        return 0
    elif y > 0:
        if x > 0:
            return p(x,y)
        elif x < 0:
            return -abs(p(x,y))
    else:
        if x > 0:
            return n(x,y)
        elif x < 0:
            return -abs(n(x,y))
        
angka = int(input('masukkan angka: '))
pangkat = int(input('masukkan pangkat: '))

print('hasil',angka,"pangkat",pangkat,"adalah",hasil(angka,pangkat))
