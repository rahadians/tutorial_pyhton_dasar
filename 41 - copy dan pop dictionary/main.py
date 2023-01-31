#copy dictionary


data_dict={
    "cup" :"Ucup surucup",
    "tong": "Otong surotong",
    "dung" : "dudung surudung"
}

data_dict_copy=data_dict.copy()

print(data_dict)

data_dict["cup"]="ncup ncup"
print(data_dict_copy)
print(data_dict)


#pop dictionary (menghapus data sesuai key yang diminta)
dataDung=data_dict_copy.pop("dung")
print (data_dict_copy)

#pop item dictionary (menghapus data yang terakhir)
#popitem adalah mengambil/menghilangkan data terakhir
dataTerakhir =data_dict_copy.popitem()
print(dataTerakhir)
print(data_dict_copy)
