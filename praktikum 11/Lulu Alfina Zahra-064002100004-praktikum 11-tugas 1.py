@author: lulualfina15
"""

class siswa:
    
    jumlah = 0
    
    def __init__(self,nama,tahun):
        self.nama = str.upper(nama)
        self.tahun = str(tahun)
        siswa.jumlah += 1
        
    def biodata(self):
        return str(f'{self.nama} ; {self.tahun}')
    
    def cetak(self):
        print()
        print('Nama:',self.nama)
        print('Tahun:',self.tahun)
        print()
        input(f'Jumlah siswa adalah {siswa.jumlah} orang\nPRESS ENTER')


while True:
    print(f'\nsiswa {(siswa.jumlah)+1}\nKetik -2 untuk berhenti!')
    x = str(input('Nama: '))
    if x == '-2':
        break
    y = str(input('Tahun: '))
    n = siswa(x,y)
    
    n.cetak()
