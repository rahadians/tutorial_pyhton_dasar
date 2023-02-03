import os
os.system("cls")

data_0 =[1,2]
data_1=[3,4]

data_2D=[data_0,data_1]


#mengambil data luar
data_ke_0=data_2D[0] #ini hanya mengambil data luarnya 
print(data_ke_0)

#mengabil data dalamnya
data_ke_0_0=data_2D[0][0]
print(data_ke_0_0)


#mengcopy nested list
data_2D_copy=data_2D.copy()

print(f"data 2D \t: {data_2D}")
print(f"data 2D Copy \t: {data_2D_copy}")

address_data_2D=hex(id(data_2D))
address_data_2D_copy=hex(id(data_2D_copy))
print(address_data_2D)
print(address_data_2D_copy)
#walaupun addressnya berbeda tetapi list dalamnya masih sama 
# jadi kalau datanya berubah akan berubah juga
address_data_2D=hex(id(data_2D[0]))
address_data_2D_copy=hex(id(data_2D_copy[0]))
print(address_data_2D)
print(address_data_2D_copy)

#Untuk copy nested list harus pakai deepcopy dengan import terlebih dahulu
from copy import deepcopy

data_deep_2D=[data_0,data_1,10]
data_deep_2D_copy=deepcopy(data_deep_2D)
print(data_deep_2D)
print(data_deep_2D_copy)
address_data_2D=hex(id(data_deep_2D[0]))
address_data_2D_copy=hex(id(data_deep_2D_copy[0]))
print(address_data_2D)
print(address_data_2D_copy)

###Jadi kalau ingin mengcopy list yang nested atau list dalam list harus pakai deepcopy
### tidak bisa hanya pakai copy saja




