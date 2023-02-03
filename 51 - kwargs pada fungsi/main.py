'''*kwargs pada fungsi'''
import os

os.system("cls")

# Fungsi Biasa
def fungsi(nama,tinggi,berat):
    '''Fungsi Biasa'''
    print(f"{nama} punya tinggi {tinggi} dan beratnya {berat}")
fungsi("ucup",183,80)



def fungsi_kwargs(**kwargs):
    '''Fungsi *kwargs '''
    print(kwargs)
    nama=kwargs["nama"]
    tinggi=kwargs["tinggi"]
    berat=kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan beratnya {berat}")
fungsi_kwargs(nama="Otong",tinggi=170,berat=60)

# Studi kasus
def math(*args,**kwargs):
    output=1
    if kwargs["option"]=="tambah":
        for element in args:
            output+=element
    elif kwargs["option"]=="kali" :
        for element in args:
            output *=element
    else:
        print("Tidak Ada Operasi")
    return output


hasil=math(1,2,3,4,5,6,option="tambah")
print(f"Hasil Jumlah {hasil}")

hasil=math(1,2,3,4,5,6,option="kali")
print(f"Hasil perkalian {hasil}")
  