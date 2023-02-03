import os
os.system("cls")

data_angka=[5,6,9,8,5,1,6,7,6,0,5,5]

print(f"data angka={data_angka}")

#count data
jumlah_data_6 = data_angka.count(6)
print(jumlah_data_6)
jumlah_data_5 = data_angka.count(5)
print(jumlah_data_5)

#ambil posisi index data
data_orang=["Ucup","Otong","Dudung","Ujang"]
print(data_orang)

index_Dudung=data_orang.index("Dudung")
print(index_Dudung)

# mengurutkan list ascending
data_angka.sort()
print(data_angka)

# mengurutkan list descending
#harus di sort ascending terlebih dahulu baru direverse
data_angka.reverse()
print(data_angka)