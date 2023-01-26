#program list buku


list_buku=[]
while True:
    print(f"Masukkan data buku")
    

    judul=input("Masukkan judul buku \t: ")
    penulis=input("Masukkan nama penulis \t: ")

    buku_baru=[judul,penulis]
    list_buku.append(buku_baru)

    print(list_buku)

    print ("No.\t| Judul \t\t|penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index+1}\t |{buku[0]}\t\t | {buku[1]}")

    print(f"==========")

    isLanjut=input("Apakah mau melanjutkan (y/n)?")

    if isLanjut=="n":
        break

print("Program Selesai")
               

