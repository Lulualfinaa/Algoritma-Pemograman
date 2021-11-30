def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1):
                if arr[j] > arr[j+1] : 
                        arr[j], arr[j+1] = arr[j+1], arr[j]

def binarySearchAppr (sor, start, end, x):
   if end >= start:
      mid = start + (end- start)//2
      if sor[mid] == x:
          return mid
      elif sor[mid] > x:
          return binarySearchAppr(sor, start, mid-1, x)
      else:
          return binarySearchAppr(sor, mid+1, end, x)
   else:
      return -1
  
arr = [3,7,25,10,6]
y = input('masukkan angka: ')
y = int(y)
bubbleSort(arr)
result = binarySearchAppr(arr, 0, len(arr)-1,y)
result = int(result)
print('data menjadi terurut:', arr)
if result != -1:
    print('angka terdapat di indeks:'+str(result))
else:
    print('angka tidak ada di arr')
