#Default Argument fungsi

# contoh 1
# memberikan argument default nama="Kamu"
def say_hello(nama="Kamu"):
    print(f"Hallo {nama}")

say_hello("ucup")
say_hello()


# contoh 2
def sapa_dia(pesan,nama="Santoso"):
    '''fungsi dengan satu input biasa, dan satu default'''
    print(f"hai {pesan}, {nama}")


sapa_dia("kamu","rahadian")
sapa_dia("kamu")


# contoh 3

def hitung_pangkat(angka=1,pangkat=1):
    hasil=angka**pangkat
    return hasil

print(hitung_pangkat(5,2))
##urutan bisa dibolak balik asal memasukkan argument
print(hitung_pangkat(pangkat=3,angka=2))

# contoh 4
def fungsi_angka(input1=1,input2=2,input3=3,input4=4):
    hasil=input1+input2+input3+input4
    return hasil

print(fungsi_angka(input4=60))