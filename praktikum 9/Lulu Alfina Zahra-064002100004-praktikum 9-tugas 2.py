@author: lulualfina15
"""

title = str(input("masukkan judul file:"))
filename = (f"{title}.txt")
f = open(filename, "w")
f.close()
print(f"FILE {filename} sudah dibuat ")
print("masukkan p untuk berhenti")

def write(string):
    file = open(f"{title}.txt","w")
    file.write(str(string))
    file.close()

def read ():
    file = open(f"{title}.txt", "r")
    teks = file.read()
    print(teks)

x = True
while x == True:
    y = (input(""))
    if y == "p":
        print("\nteks sudah disimpan")
        x = False
    else:
        write(y)
        read()
