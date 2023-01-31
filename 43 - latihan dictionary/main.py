# Latihan Dictionary part 1

#Formkey
#templat dict mahasiswa

import datetime
import os
import string
import random


# memerintahkan ketik cls via python
os.system("cls") #ketik cls di terminal

mahasiswa_template={
        'nama':'nama',
        'nim' : 00000000,
        'sks_lulus':0,
        'lahir':datetime.datetime(1111,11,11)
 }

# dictionary kosong
data_mahasiswa ={} 

while True :
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'Data Mahasiswa':^20}")
    print("-"*60)

    mahasiswa =dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama']=input("nama Mahasiswa : ")
    mahasiswa['nim']=input("NIM Mahasiswa : ")
    mahasiswa['sks_lulus']=int(input("SKS Lulus : "))
    tahunLahir=int(input("Tahun Lahir (YYYY): "))
    bulanLahir=int(input("Bulan Lahir (MM): "))
    tanggalLahir=int(input("Tanggal Lahir (DD): "))
    mahasiswa['lahir']=datetime.datetime(tahunLahir,bulanLahir,tanggalLahir)


    KEY= ''.join(random.choice(string.ascii_uppercase) for i in range(6))

    data_mahasiswa.update({KEY:mahasiswa})
    print("\n")
    print(f"{'KEY':<6} {'NAMA' :<17} {'SKS':<3} {'LAHIR':<10}")
    print("-"*20)

    for element in data_mahasiswa:        
        KEY= element

        NAMA =data_mahasiswa[KEY]['nama']
        NIM =data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']        
        LAHIR=data_mahasiswa[KEY]['lahir'].strftime('%x')

        print(f"{KEY:<6} {NAMA :<17} {SKS:<3} {LAHIR:<10}")

    print("\n")        
    isDone = input("Apakah Ada Data Lain (y/n) ?")
    if isDone=="n":
        break

    
print("Aplikasi sudah selesai")