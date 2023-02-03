import os
os.system("cls")

data_0 = [1,2]
data_1=["Oring","Dadang"]

list_2D=[data_0,data_1]
print(list_2D)


list_2D_campur=[data_0,data_1,True,False]
print(list_2D_campur)

#contoh penggunaannya

peserta_0=["Ucup",25,"Laki-Laki"]
peserta_1=["Otong",20,"Laki-Laki"]
peserta_2=["Oneng",25,"Perempuan"]

list_peserta=[peserta_0,peserta_1,peserta_2]
print(list_peserta)

#jika ingin print nama peserta

for peserta in list_peserta:
    print(f"nama peserta \t: {peserta[0]}")
    print(f"umur peserta \t: {peserta[1]}\n")

#Permasalahan denga reference walau dengan copy adressnya tetap sama
list_copy=list_peserta.copy()
print(list_copy)
#diubah index 0 dengan nama rahadian
peserta_0[0]="rahadian"
print(list_copy)
print(list_peserta)
