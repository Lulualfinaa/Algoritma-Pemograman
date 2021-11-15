def ordinalNumber(y):
    rumus = lambda y :"(%d, '%s')" % (y,{1:"st",2:"nd",3:"rd"}.get(y if y < 20 else y % 10,"th"))
    print("ordinal number: "+(rumus(y)))

print("membuat Ordinal Number")
print("Ketik (0) untuk berhenti")
loop = True
while loop == True:
    y = int(input("Masukkan Angka : "))
    if y == 0 :
        loop = False
        break
    else:
        ordinalNumber(y)
