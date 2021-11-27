
#Buat list sebanyak 5 elemen dengan nilai bebas
list1 = [1, 2, 3, 4, 5]

#Tampilkan elemen ke 3
print(list1[2])

#Ambil nilai elemen ke 2 sampai elemen ke 4
print(list1[1:3])

#Ambil element terakhir
print(list1[4])

print()

#Ubah elemen ke 4 dengan elemen lainnya
list1[3] = [8]
print(list1[3])

#Ubah elemen ke 4 sampai dengan elemen terakhir 
list1[3:] = 9 , 10
print(list1[3:]) 

print()

#Ambil 2 bagian dari list pertama(A) dan dijadikan list ke 2(b)
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40,50]
print(list1[:2] + list2)

print()

#Tambah list B dengan nilai string
list2 = [10, 20, 30, 40, 50, 'Hello']
print(list2)

print()

#Gabungkan list b dengan list a
print(list1 + list2)



