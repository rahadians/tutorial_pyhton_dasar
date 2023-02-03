'''membuat module'''


# cara lebih elegan untuk import
## cara 1 mengambil sebagian
from matematika import tambah,kali,pangkat


## cara 2 untuk mengambil sebagian
from matematika import tambah
from matematika import kali
from matematika import pangkat

##cara 3 untuk mengambil semua
from matematika import * 

hasil_tambah=tambah(4,5,6,7,8,9)
print(f"hasil tambah = {hasil_tambah}")


hasil_kali=kali(4,5,6,7,8,9)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = pangkat(3)
print (f"hasil pangkat3={pangkat_3(3)}")


