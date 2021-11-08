@author: lulualfina15
"""

print('menentukan jumlah hari dalam satu bulan sesuai tahun')
def angkaBulan(bulan):
        if bulan in [1,2,3,4,5,6,7,8,9,10,11,12]:
            if bulan == 2:
                tahun = int(input('masukkan tahun : '))
                angkaTahun(tahun)
            else:
                if bulan in [1,3,5,7,8,10,12]:
                    print('terdapat 31 hari dalam sebulan')
                else:
                    print('terdapat 30 hari dalam sebulan')
        else:
            print(f'INVALID masukkan nilai : {bulan}')

def angkaTahun(tahun):
        if tahun%4==0:
            print('terdapat 29 hari dalam sebulan')
            print('merupakan tahun kabisat')
        else:
            print('terdapat 28 hari dalam sebulan')

loop = True
while loop == True:
    print('-2 untuk berhenti!')
    bulan = int(input('masukkan bulan (1-12): '))
    if bulan== -2:
        loop = False
        print('terima kasih')
    else:
        angkaBulan(bulan)
