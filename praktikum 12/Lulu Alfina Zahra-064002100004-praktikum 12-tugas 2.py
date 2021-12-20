@author: lulualfina15
"""

print("===============================================")
print("PROGRAM MEMBUAT DATA MEAN DAN STANDAR DEVISIASI")
print("===============================================")

title = str(input("MASUKAN JUDUL FILE:"))
filename = (f"{title}.csv")
f = open(filename, "w")
f.close()

print(f"FILE {filename} TELAH DIBUAT!!")
print("PRESS S untuk berhenti")

file = open('Negara.csv','r')

class my_dictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

data = my_dictionary()
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []

x = 0
for cache in file:
    x += 1
    cache = cache.split(',')
    if x == 1:
        pass
    else:
        p1 = cache[0]
        a1.append(p1)
        p2 = cache[1]
        a2.append(p2)
        p3 = cache[2]
        a3.append(p3)
        p4 = int(cache[3])
        a4.append(p4)
        p5 = int(cache[4])
        a5.append(p5)

data.add('Negara',a1)
data.add("Ibu Kota",a2)
data.add('Benua',a3)
data.add('Luas',a4)
data.add('Populasi',a5)

import pandas as DATAFILE

def write(string):
    file = open(f"{title}.csv","w")
    file.write(str(string))
    file.close()

def read ():
    file = open(f"{title}.csv", "r")
    teks = file.read()
    print(teks)

X = True
while X == True:
    hasil = DATAFILE.DataFrame(data)
    print('\nLUAS DAN POPULASI NEGARA DITIAP DUNIA\n\n',hasil)
    print("input 1 untuk mencari data mean")
    print("input 2 untuk mencari standart devisiasi")
    
    isi = int(input("masukan pilihan:"))
    mean = hasil.groupby(['Benua']).mean()
    std = hasil.groupby(['Benua']).std()
    if isi == 0:
        print("\nTEKS TELAH TERSIMPAN")
        X = False
    elif isi == 1:
        print('\nRata-rata data:\n',mean)
        write(mean)
        read()
    elif isi == 2:
        print('\nStandar Deviasi:\n',std)
        write(std)
        read()
