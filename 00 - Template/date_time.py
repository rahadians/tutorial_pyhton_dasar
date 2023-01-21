# Data dan time (latihan)

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)


print("Silahkan masukkan tanggal, \nbulan, dan tahun")

tanggal = int(input("Tanggal \t:"))
bulan = int(input("bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))


tanggal_lahir = dt.date(tahun, bulan, tanggal)

print(f"tanggal_lahir anda adalah {tanggal_lahir}")


hari_ini = dt.date.today()

print(f"Hari ini adalah : {hari_ini}")

umur = (hari_ini-tanggal_lahir)/365

umur_tahun = umur.days


print(f"Umur anda adalah : {umur_tahun}")
