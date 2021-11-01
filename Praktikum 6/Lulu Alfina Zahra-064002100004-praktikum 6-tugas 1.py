@author: lulualfina15
"""

nilai = [ 4.00 , 3.75 , 3.50 , 3.00 , 2.75 , 2.50 , 2.00 , 1.75 , 1.50 , 1.25]

def vartoscore(y):
    
    if y == 'A':
        score = float(nilai[0])
    elif y == 'A-':
        score = float(nilai[1])
    elif y == 'B+':
        score = float(nilai[2])
    elif y == 'B':
        score = float(nilai[3])
    elif y == 'B-':
        score = float(nilai[4])
    elif y == 'C+':
        score = float(nilai[5])
    elif y == 'C':
        score = float(nilai[6])
    elif y == 'C-':
        score = float(nilai[7])
    elif y == 'D':
        score = float(nilai[8])
    elif y == 'E':
        score = float(nilai[9])
    else:
        print('INVALID SCORE!')
        score = 0
    return score
        
def rata2(datanya):
    total = sum(datanya)
    rata2 = float(total / len(datanya))
    return rata2

def masukkandata():
        variabelnilai = str.upper(input('"exit" untuk berhenti!\nMasukkan nilai siswa: '))
        return variabelnilai
    
def hasil():    
    print(('''
          
          
          Nilai siswa:
          {0}
          
          Jumlah siswa: {1}
          
          Total nilai: {2}
          
          Rata-rata nilai = {3}
          
          
          ''').format(datanilai,len(datanilai),sum(datanilai),rata2(datanilai)))
    
datanilai = []
ulang = 0
nomor = 0
while ulang == 0:
    nomor += 1
    nilaivariabel = masukkandata()
    if nilaivariabel == 'EXIT':
        ulang = 1
    else:
        s = vartoscore(nilaivariabel)
        print(('Siswa ke-{0} = {1}').format(nomor,s))
        datanilai.append(s)
          
hasil()
