@author: lulualfina15
"""

def fibbo(n):
   if n <= 1:
       return n
   else:
       return(fibbo(n-1) + fibbo(n-2))
   
def cetak(x):
    if x <= 0:
        print("angka positif")
    else:
       print('Bilangan FIBBONACCI ke-'+str(x),'adalah',fibbo(x))

while True:
    try:
        bil = int(input('Masukkan bilangan:'))
    except ValueError:
        print('Invalid input, masukkan angka bulat\n')
    else:
        cetak(bil)
