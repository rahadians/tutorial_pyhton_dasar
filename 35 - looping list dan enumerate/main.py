#Looping dari list
#Cara looping dari list dengan cara:
# 1. for loop
print("For Loop")
kumpulan_angka=[1,5,8,9,8,7,0]
for angka in kumpulan_angka:
    print (angka)    
print("==========\n")

# 2. for loop dan range
print("For Loop dan range")
kumpulan_angka=[1,5,8,9,8,7,0]
panjang=len(kumpulan_angka)
for angka in range(panjang):
    print(angka)
print("==========\n")

# 3.while
print("While")
kumpulan_angka=[1,5,8,9,8,7,0]
panjang=len(kumpulan_angka)
angka=0

while angka<panjang:
    print(angka)
    angka +=1
print("==========\n")

# 4.list comprehension ini adalah cara yang paling singkat
# selain itu juga bisa membuat list baru dengan operasional

print("List Comprehension")
kumpulan_angka=[1,5,8,9,8,7,10]
[print(f"data = {angka}") for angka in kumpulan_angka]
[print(f"angka kuadrat = {angka**2}") for angka in kumpulan_angka]




print("==========\n")


#enumerate bisa mendapatkan index dan angka
print("enumerate")
kumpulan_angka=[1,5,8,9,8,7,0]

for index,angka in enumerate(kumpulan_angka):
    print(f"index= {index}, angka= {angka}")
print("==========\n")


