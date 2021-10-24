@author: lulualfina15
"""

print('''
===================================
SELAMAT DATANG DI KEBUN BINATANG
===================================
Daftar harga tiket:
1. umur <= 2 tahun          : $FREE
2. umur 3 - 12 tahun        : $14
3. umur 13 - 65 tahun       : $23
4. umur >= 65 tahun         : $18
===================================
    ''')
total = 0
while True:
    try:
        umur = int(input("Masukkan umur anda: "))
    except ValueError:
        break
    if umur <= 2:
            print("FREE")
    elif umur in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            total += 14
            print("Harga $14")
            print(f"Running total : ${total}")
    elif umur >= 65:
            total += 18
            print("Harga $18")
            print(f"Running total : ${total}")
    else:
            total += 23
            print("Harga $23")
            print(f"Running total : ${total}")
            
uang = int(input("Masukkan uang anda: "))
if uang > total:
    bayar = uang - total
    print(f"Kembalian : ${bayar}")
elif uang < total:
    bayar = total - uang
    print(f"Uang anda kurang ${bayar}")
else:
    print("Uang anda pas, terima kasih")

