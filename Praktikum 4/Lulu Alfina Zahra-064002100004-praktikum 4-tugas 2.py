x = True
while x == True:

    bulan = int(input("Masukkan Bulan(angka): "))
    if bulan == 0 or bulan > 12:
        print("invalid")
    else:
        tahun = int(input("Masukkan Tahun(angka): "))
        hari = ["none"]
        for i in range(6):
            hari.append(31)
            hari.append(30)

        tahunstr = str(tahun)

        if tahunstr[-1] == "0" and tahunstr[-2] == '0':
            tahun = tahun/100
            sisa = tahun % 4
            if sisa == 0:
                print('\nKabisat')
                hari[4] = 29
            else:
                print('\nNormal')

        else:
            sisa = tahun % 4
            if sisa == 0:
                print('\nKabisat')
            else:
                print('\nNormal')

        print(('Jumlah hari pada bulan {0}: {1}').format(bulan,hari[bulan]))
        ops = input('Press ENTER(lanjut) atau masukkan "n" untuk berhenti ')
        if ops == 'n':
            x = False
