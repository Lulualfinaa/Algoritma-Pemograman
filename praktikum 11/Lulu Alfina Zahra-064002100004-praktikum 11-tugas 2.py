@author: lulualfina15
"""

class mahasiswa:

    jumlah = 0

    def __init__(self,nama,nim,jurusan):
        self.__nama = str.upper(nama)
        self.__nim = str(nim)
        self.__jurusan = str(jurusan)
        mahasiswa.jumlah += 1

    def biodata(self):
        return f"{self.nama} ; {self.nim} ; {self.jurusan}"

    def cetak(self):
        print()
        print('Nama:',self.__nama)
        print('NIM:',self.__nim)
        print('Jurusan:',self.__jurusan)
        print()
        input(f'Jumlah mahasiswa adalah {mahasiswa.jumlah} orang\nPRESS ENTER')

class gettermethod:
    jumlah = 0
    #gettermetod
    def __init__(self,nama,nim,jurusan):
        self.__nama = str.upper(nama)
        self.__nim = str(nim)
        self.__jurusan = str(jurusan)
        mahasiswa.jumlah += 1

    def biodata(self):
        return f"{self.nama} ; {self.nim} ; {self.jurusan}"

    def cetak(self):
        print()
        print('Nama:',self.__nama)
        print('NIM:',self.__nim)
        print('Jurusan:',self.__jurusan)
        print()
        input(f'Jumlah mahasiswa adalah {mahasiswa.jumlah} orang\nPRESS ENTER')
    def nama(self):
        return self.__nama
    def nim(self):
        return self.__nim
    def jurusan(self):
        return self.__jurusan

class settermethod:  
    jumlah = 0
    jumlah = 0
    #gettermetod
    def __init__(self,nama,nim,jurusan):
        self.__nama = str.upper(nama)
        self.__nim = str(nim)
        self.__jurusan = str(jurusan)
        mahasiswa.jumlah += 1

    def biodata(self):
        return f"{self.nama} ; {self.nim} ; {self.jurusan}"

    def cetak(self):
        print()
        print('Nama:',self.__nama)
        print('NIM:',self.__nim)
        print('Jurusan:',self.__jurusan)
        print()
        input(f'Jumlah mahasiswa adalah {mahasiswa.jumlah} orang\nPRESS ENTER')
    #settermethod
    def nama(self, x):
        self.__nama = x

    def nim(self, y):
        self.__nim = y   

    def jurusan(self,z):
        self.__jurusan = z

while True:
    print("ketik -2 untuk method getter")
    print("ketik -1 untuk method setter")
    print(f'mahasiswa {(mahasiswa.jumlah)+1}\nKetik angka selain -2 atau -1 untuk berhenti')
    method = int(input('Maasukkan pilihan (-2,-1): '))

    if method == -2:
        print(f'\nmahasiswa {(mahasiswa.jumlah)+1}')
        print("kamu menggunakan method getter")
        x = str(input('Masukkan nama: '))
        y = str(input('Masukkan nim: '))
        z = str(input('Masukkan jurusan: '))
        n = gettermethod(x,y,z)
        n.cetak()

    elif method == -1:
        print(f'\nmahasiswa {(mahasiswa.jumlah)+1}')
        print("kamu menggunaakan method setter") 
        x = str(input('Masukkan nama: '))
        y = str(input('Masukkan nim: '))
        z = str(input('Masukkan jurusan: '))
        n = settermethod(x,y,z)
        n.cetak()

    else :
        break
