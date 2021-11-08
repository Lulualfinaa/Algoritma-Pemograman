@author: lulualfina15
"""

def cekBilangan(bil):
    if bil == 1:
        print(f"Bilangan ini {bil} adalah prima")
    elif bil == 2:
        print(f"Bilangan ini {bil} adalah prima")
    else:
        global z 
        for x in range(2, bil):
            if bil % z == 0:
                stat = 0 
                break
            else:
                stat = 1 
        cekStat(stat)
        
def cekStat(stat):
    if stat == 0:
        print(f"Bilangan ini {bil} adalah prima")
        print(f"{z} kali {bil//z} = {bil}")
    else:
        print(f"{bil} adalah prima")

z = 1
while z == 1:                    
    bil = int(input("Masukkan bilangan : "))
    cekBilangan(bil)                 
bil = int(input("Masukkan bilangan : "))
cekBilangan(bil)
