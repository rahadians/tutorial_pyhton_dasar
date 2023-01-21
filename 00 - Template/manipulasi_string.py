# operator dalam bentuk methods


# merubah case dari string


# merubah semua ke upper case


salam = "bro"

print("normal = ", salam)

salamUpper = salam.upper()
salamLower = salam.lower()
print(salamUpper)
print(salamLower)

# pengecekan dengan isX methode

# contoh untuk pengecekan lowercase

salam = "sist"
apakah_lower = salam.islower()

print(apakah_lower)

# isalpha() --> untuk mengecek semua huruf
# isalnum()--> huruf dan angka
# isdecimal()--> angka saja
# isspace()--> spasi, tab, newline \n
# istitle()--> semua kata dimulai dengan huruf besar

# mengecek komponen

cek_start = "Sangjangnim Oppa".startswith("Sang")
print(cek_start)

cek_end = cek_start = "Sangjangnim Oppa".endswith("Oppa")
print(cek_end)

# Penggabungan komponen join() split()
pisah = ["aku", "sayang", "kamu"]
print(pisah)


gabungan = ';'.join(pisah)

print(gabung)


gabung+"akusayangkamu"
print(gabungan)
