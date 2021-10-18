Created on Mon Oct 18 12:44:55 2021

@author: lulualfina15
"""

n = [ 4.00 , 3.75 , 3.50 , 3.00 , 2.75 , 2.50 , 2.00 , 1.75 , 1.50 , 1.25]
skor = 0

        
nsiswa = []

ulang = 0
nomor = 0
while ulang == 0:
    nomor += 1
    x = str.upper(input('"q" keluar!\nn siswa: '))
    if x == 'Q':
        ulang = 1
    else:
        if x == 'A':
            skor = float(n[0])
        elif x == 'A-':
            skor = float(n[1])
        elif x == 'B+':
             skor = float(n[2])
        elif x == 'B':
            skor = float(n[3])
        elif x == 'B-':
            skor = float(n[4])
        elif x == 'C+':
            skor = float(n[5])
        elif x == 'C':
            skor = float(n[6])
        elif x == 'C-':
            skor = float(n[7])
        elif x == 'D':
            skor = float(n[8])
        elif x == 'E':
            skor = float(n[9])
        else:
            print('Saya tidak mengerti...')
            skor = 0
        print(('\nMurid{0} = {1}').format(nomor,skor))
        nsiswa.append(skor)

rata2 = sum(nsiswa) / len(nsiswa)
print('Rata rata n:', rata2)
