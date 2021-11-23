@author: lulualfina15
"""

def write(x):
    file = open('file_biodata.txt', 'w')
    file.write(str(x))
    file.close()
    
def read():
    file = open('file_biodata.txt','r')
    print(file.read())
    file.close()
    
A = str(input('nama anda: '))
B = str(input('umur anda: '))
C = str(input('alamat anda: '))
D = str(input('email anda: '))
E = str(input('dosen wali anda: '))
bio = str(f'''
          
nama = {A}
umur = {B}
alamat = {C}
email = {D}
dosen wali = {E}''')

print('\ntulis data anda')
write(bio)
read()      
