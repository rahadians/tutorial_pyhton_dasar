## Teknik menduplikat list

import os
os.system("cls")

data_orang=["Ucup","Otong","Dudung"]
print(f"data_orang_lama = {data_orang}")

#copy data_orang ke baru
data_orang_baru=data_orang

print(f"data orang baru = {data_orang_baru}")

#Jika member diganti
data_orang[1]="Rahadian"

print(f"data orang lama = {data_orang}")
print(f"data orang baru = {data_orang_baru}")

#cara diatas adalah karena alamat address sama walaupun dicopy
print(f"data address data orang = {hex(id(data_orang))}")
print(f"data address data orang baru = {hex(id(data_orang_baru))}")

#copy list yang benar adalah dengan menduplicate agar address memory berbeda

data_orang_baru=data_orang.copy()
print(f"data orang lama = {data_orang}")
print(f"data orang baru = {data_orang_baru}")
print(f"data address data orang = {hex(id(data_orang))}")
print(f"data address data orang baru = {hex(id(data_orang_baru))}")