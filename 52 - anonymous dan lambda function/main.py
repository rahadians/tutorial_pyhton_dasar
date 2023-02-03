# anonymous dan lambda function
import os
os.system("cls")

# fungsi biasa
def f_kuadrat(angka):
    return angka**2

print(f"Hasil fungsi kuadrat adalah {f_kuadrat(3)}")

#Fungsi lambda
# output = lambda argument:expression
kuadrat = lambda angka:angka**2
print(f"ini adalah hasil kuadrat pakai lambda {kuadrat(3)}")

# lambda dengan 2 parameter
pangkat= lambda num,pow : num**pow
print(f"hasil lambda pangkat 2 parameter 4^2 = {pangkat(4,2)}")

# kegunaan lambda
## 1. sorting untuk list

data_list=["Otong","Ucup","Dudung","Cucu"]

# sorting biasa
data_list.sort()
print(f"sorting data list biasa {data_list}")



# Sorting berdasarkan jumlah karaketer
##sorting biasa
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorting data list biasa berdasarkan panjang karakter {data_list}")


##Sort pakai lambda
data_list=["Otong","Ucup","Dudung","Ucu"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorting data list lambda berdasarkan panjang karakter {data_list}")

# 2. Filter

## kasus filter biasa
data_angka=[1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka<5

###cara biasa
data_angka_baru=list(filter(kurang_dari_lima,data_angka))
print(f"hasil data angka baru filter biasa= {data_angka_baru}")
###cara lambda
data_angka_baru=list(filter(lambda i:i<5,data_angka))

print(f"hasil data angka baru filter lambda= {data_angka_baru}")


###Kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(f"hasil data angka baru filter angka genap lambda= {data_genap}")

###kasus ganjil
data_genap = list(filter(lambda x:(x%2!=0),data_angka))
print(f"hasil data angka baru filter angka ganjil lambda= {data_genap}")

#anonymous function
#currying <- Haskell Curry

###fungsi biasa
def pangkat(angka,n):
    hasil=angka**n
    return hasil
data_hasil=pangkat(5,2)
print(f"Fungsi biasa = {data_hasil}")

###dengan currying 

def pangkat(n):
    return lambda angka:angka**2

pangkat2=pangkat(2)
print(f"pangkat2 ={pangkat2(5)}")

pangkat3=pangkat(3)
print(f"pangkat3 = {pangkat3(3)}")

# atau bisa langsung
print(f"pangkat bebas = {pangkat(4)(5)}")