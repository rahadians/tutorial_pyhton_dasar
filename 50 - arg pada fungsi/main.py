'''*args'''

# memasukkn data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi ("ucup",170,40)

'''fungsi ribet'''
def fungsi_list(data_list):
    data=data_list.copy()
    nama=data[0]
    tinggi=data[1]
    berat=data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi_list(["suruciup",100,40])

# kenalan dengan *args cara lain memanggil list tidak perlu pakai []
def fungsi_args(*args):
    nama=args[0]
    tinggi=args[1]
    berat=args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi_args("otong",170,80)

# studi kasus

# bisa pakai *args bisa ganti nama apa saja yang penting depannya * contoh *data
def tambah(*data):
    print(len(data))
    output=0
    for element in data:
        output+=element
    return output

hasil=tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")