a=int(input("masukkan sisi a: "))
b=int(input("masukkan sisi b: "))
c=int(input("masukkan sisi c: "))

if a == b == c :
    print("segitiga sama sisi")
elif (a + b <= c) or (a + c <= b) or (b + c <= a) :
    print("bukan segitiga")
elif a == b or a == c or b == c :
    print("segitiga sama kaki")
elif a*a + b*b == c*c or a*a -c*c == b*b or c*c - b*b == a*a :
    print("segitiga siku - siku")

else:
    print("segitiga sembarang")
    
