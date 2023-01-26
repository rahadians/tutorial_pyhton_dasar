# ---LIST---

# kumpulan data numbers

data_angka=[1,2,3]
print(data_angka)




#kumpulan data string
data_string =["ucup","otorng","odah"]
print(data_string)


data_boolean =[True,False,True,False]
print(data_boolean)


data_campuran=[1,True,"Bambang"]
print(data_campuran)



##Data Range
data_range=range(0,10)
print(data_range)
data_list =list(data_range)
print(data_list)

data_range_increment=range(0,20,2)
print(data_range_increment)
data_list_increment=list(data_range_increment)
print(data_list_increment)


#membuat list dengan for loop, disebut list comprehensip

list_pake_for=[i for i in range(0,20)] 
print(list_pake_for)

list_pake_for_kuadrat=[i**2 for i in range(0,20)] 
print(list_pake_for_kuadrat)

#list pakai for pakai if

list_pake_for_if = [i for i in range(1,10) if i!=5]
print(list_pake_for_if)

list_pake_for_if_genap = [i for i in range(1,10) if i%2==0]
print(list_pake_for_if_genap)



