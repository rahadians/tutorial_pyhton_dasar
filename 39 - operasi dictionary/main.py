#Opoerator dictionary

data_dict={
    "cup" :"Ucup surucup",
    "tong": "Otong surotong",
    "dung" : "dudung surudung"
}

#cek banyaknya item
lendict= len(data_dict)
print(lendict)

#mengecek key exist atau tidak
key="tong"
checkkey=key in data_dict
print(checkkey)

# mengakses value (read) dengan get
# pakai get untuk membedakan apakah dia dictionary atau bukan
# mencari apakah key ada atau tidak
print(data_dict.get("cup"))
print(data_dict.get("cupp","Key Tidak ditemukan")) #bisa dimasukkan message

# mengupdate data dictionary
data_dict["cup"]="Ucup mantap"
print(data_dict)

# Menambah/update data di data_dict
data_dict["sep"]="Asep surecep"
print(data_dict)
data_dict.update({"rahad":"rahadian santosoo"})
print(data_dict)

#menghapus data dari dictionary
del data_dict["sep"]
print(data_dict)