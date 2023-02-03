'''Global dan local scope'''

import os
os.system("cls")

# nama Disebut variable global
nama_global="Otong" 

#Akses variable global dalam fungsi
def fungsi_1():
    print(f"Fungsi menampilkan {nama_global} ")

fungsi_1()

# akses variable global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabangan

if True:
    print(f"if menampilkan {nama_global}")



## Variable Local Scope adalah variable yang didescripsikan di dalam fungsi
def fungsi_2():
    nama_local="Ucup"

fungsi_2()
#   print(f"if menampilkan {nama_local}")  --> ini salah karena nama_local didesc dalam fungsi

##contoh  penggunaan
###contoh 1
def say_otong():
    print(f"Hello {nama}")

nama="Otong"
say_otong()


###contoh 2 : merubah variable global
# local variable hanya berlaku pada fungsi, tidak berlaku for loop atau if

angka=0

def ubah_angka(nilai_baru):
    angka=nilai_baru #angka tidak dapat diubah karena dianggap local variable

    global hasil #global mengubah local variable menjadi global
    hasil=nilai_baru
    return hasil

print(f"Sebelum {angka}")
ubah_angka(10)
print(f"sesudah {angka}")

ubah_angka(20)
print(f"angak berubah menjadi global variable {hasil}")

