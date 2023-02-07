# cukup panggil foldernya saja karena sudah dipanggil di __init__.py
import sains

hasil_tambah = sains.matematika.basic.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}")

hasil_fisika = sains.fisika.gaya(10,9.8)
print(f"hasil fisika dari package adalah = {hasil_fisika}")