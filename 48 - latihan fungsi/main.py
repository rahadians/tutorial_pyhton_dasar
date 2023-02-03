'''Latihan Fungsi'''

import os

#program untuk menghitung luas dan keliling persegi panjang

#membuat header program



# ini cara panjangnya
os.system('cls')
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print (f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'='*40:^40}")

# #mengambil input user
# lebar = int(input("Masukkan nilai lebar : "))
# panjang = int(input("Masukkan nilai panjang : "))

# #program menghitung luas
# luas=panjang*lebar
# keliling=2*(panjang+lebar)

# print(f"hasil perhitungan Luas :  {luas}")
# print(f"hasil perhitungan Keliling :  {keliling}")

# ini cara pendeknya
def header():
    '''Fungsi Header'''
    os.system('cls')
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print (f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'='*40:^40}")

def input_user():
    '''fungsi input user'''
    lebar = int(input("Masukkan nilai lebar : "))
    panjang = int(input("Masukkan nilai panjang : "))
    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''Fungsi Luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''Fungsi keliling'''
    return 2*(lebar+panjang)

def display(message,value):
    '''fungsi display'''
    print(f"{message}= {value}")


# program utama
while True:
    header()

    lebar,panjang= input_user()
    Luas=hitung_luas(lebar,panjang)
    Keliling=hitung_keliling(lebar,panjang)

    display("hasil perhitungan Luas ",  Luas)
    display("hasil perhitungan Keliling ",  Keliling)


    isContinue=input("Apakah lanjut (y/n)? ")
    if isContinue=="n":
        break

print("Program Selesai")