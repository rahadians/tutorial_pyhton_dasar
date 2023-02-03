# ---LIST---

# kumpulan data numbers
import os

os.system("cls")


data_angka=[1,2,3]
print(data_angka)
print("="*20)

#kumpulan data string
data_string =["ucup","otorng","odah"]
print(data_string)
print("="*20)

data_boolean =[True,False,True,False]
print(data_boolean)
print("="*20)

data_campuran=[1,True,"Bambang"]
print(data_campuran)
print("="*20)


##Data Range
data_range=range(0,10)
print(data_range)
data_list =list(data_range)
print(data_list)
print("="*20)


data_range_increment=range(0,20,2)
print(data_range_increment)
data_list_increment=list(data_range_increment)
print(data_list_increment)
print("="*20)

#membuat list dengan for loop, disebut list comprehensip

list_pake_for=[i for i in range(0,20)] 
print(list_pake_for)
print("="*20)

list_pake_for_kuadrat=[i**2 for i in range(0,20)] 
print(list_pake_for_kuadrat)
print("="*20)
#list pakai for pakai if

list_pake_for_if = [i for i in range(1,10) if i!=5]
print(list_pake_for_if)
print("="*20)

list_pake_for_if_genap = [i for i in range(1,10) if i%2==0]
print(list_pake_for_if_genap)
print("="*20)
