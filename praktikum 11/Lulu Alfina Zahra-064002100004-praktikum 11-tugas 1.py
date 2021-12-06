@author: lulualfina15
"""

class mahasiswa:
    
    jumlah = 0
    
    def __init__(self,nama,nim,jurusan):
        self.nama = str.upper(nama)
        self.nim = str(nim)
        self.jurusan = str(jurusan)
        mahasiswa.jumlah += 1
        
    def biodata(self):
        return str(f'{self.nama} ;  {self.nim} ; {self.jurusan}')
    
    def cetak(self):
        print()
        print('nama:',self.nama)
        print('nim:',self.nim)
        print('jurusan:',self.jurusan)
        print()
        input(f'Jumlah mahasiswa adalah {mahasiswa.jumlah} orang\nPRESS ENTER')


while True:
    print(f'\nmahasiswa {(mahasiswa.jumlah)+1}\nKetik -2 untuk berhenti!')
    x = str(input('nama: '))
    if x == '-2':
        break
    y = str(input('nim: '))
    z = str(input('jurusan: '))
    n = mahasiswa(x,y,z)
    
    n.cetak()
