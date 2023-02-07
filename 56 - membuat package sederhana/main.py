import sains.matematika
# import sains.fisika 
# bisa pakai :

# from sains import fisika 
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}")


hasil_gaya= sains.fisika.gaya(90,10)
print(f"Gaya adalah  adalah = {hasil_gaya}")

# atau 

hasil_gaya= force(90,10)
print(f"Gaya adalah  adalah = {hasil_gaya}")