@author: lulualfina15
"""

file = open('Negara.csv','r')

class my_dictionary(dict):

    def _init_(self):
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

hasil = DATAFILE.DataFrame(data)

print('\nLUAS DAN POPULASI DUNIA\n\n',hasil)


mean = hasil.groupby(['Benua']).mean()
std = hasil.groupby(['Benua']).std()
print("============================================================================")
print('\nRata-rata data:\n',mean)
print("============================================================================")
print('\nStandar Deviasi:\n',std)
