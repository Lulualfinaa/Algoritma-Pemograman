@author: lulualfina15
"""

def bubbleSort(array):
    count = 0
    n = len(array) 
    for i in range(n): 
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                count += 1
    return array
    
    if count == 0:
        return array
    else:
        bubbleSort(array)

while True:
    while True:
        try:        
            urutkan = str(input('Masukkan angka: (3,5,11,..)\n')).split(',')
            urutkan = [int(i) for i in urutkan]
        except:
            print('\nError:\n* Error\n* bukan bil bulat')
        else:
            break
    
    print(f'\n\nList: {urutkan}')
    
    bubbleSort(urutkan)  
    print(f'\n\nList diurutkan: {urutkan}')
