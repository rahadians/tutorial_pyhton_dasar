##Operasi

import os
os.system("cls")

#index kalau dari kiri ke kanan dimulai dari 0 - dst
#index kalau dari kanan ke kiri dimulai dari -1,-2, dst



# dari kiri ke kanan   0        1       2
#data kanan ke kiri     -3      -2      -1
data_index_normal = ["Ucup","Otong","Dudung"]


data_0 =data_index_normal[0]
print(data_0)
data_terakhir =data_index_normal[-1]
print(data_terakhir)

#mengambil info jumlah data list
panjang_data=len(data_index_normal)
print(panjang_data)

#manipulasi data list

##menambahkan item pada list sesuai posisi
#data.insert(posisi,item)
data_index_normal.insert(1,"rahadian")
print(data_index_normal)


##menambah item pada posisi akhir list
data_index_normal.append("santoso")
print(data_index_normal)

## menambahkan list dengan list

data__baru=["ujang","usep","dadang"]
data_index_normal.extend(data__baru)
print(data_index_normal)

## merubah data
### merubah data ke 2 menjadi michael

data_index_normal[2]="Michael"
print(data_index_normal)

## meremove data
data_index_normal.remove("Michael")
print(data_index_normal)

## meremove data paling belakang
data_index_normal.pop()
print(data_index_normal)
