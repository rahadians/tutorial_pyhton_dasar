#List adalah contoh array di python, mengakses data dengan index

#Dictionary (dict) --> Associative array artinya bisa berubah ubah posisinya menggunakan identifier --> key biasa disebut json

data_dic={
    "key1": "value 1",
    "key2": "value 2"
}

print(data_dic)

data_dic_nama={
     "cp" :"ucup",
      "tg" :"otong",
      "dg" :"dudung",
      "nomor":100,
      "list":data_dic
}

print(data_dic_nama["tg"])
print(data_dic_nama["nomor"])
print(data_dic_nama["list"])

