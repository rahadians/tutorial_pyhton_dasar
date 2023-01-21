# Latihan perulangan membuat segitiga

# *
# **
# ***
# ****
# *****

# 1. Menggunakan for
# sisi = 5
# count=1
# for i in range(sisi) :
#     print("*" * count)
#     count +=1


# 2. Menggunakan while
# count=1
# while True : 
#     print("*" * count)
#     count +=1

#     if count==10:
#         break


# 3. menggunakan continue
# membuat segitiga hanya ganjil

# count=0
# while True:
# # akan kembali looping ke atas apabila ganjil    
#     if count ==20:
#         break
#     if (count%2):        
#         count+=1
#         continue
#     else:
#         count +=1
#         print("*" * count)
    
sisi=15
count=0
spasi=int(sisi/2)
print(spasi)  


while True:
    if count==sisi:
        break
    if(count%2):
        print(" " * spasi,"+" * count)
        spasi-=1
        count+=1
    else:
        count +=1
        continue

  


