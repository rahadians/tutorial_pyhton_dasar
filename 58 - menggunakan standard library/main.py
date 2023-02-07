import datetime

data_waktu=datetime.datetime.now()
print(data_waktu)
print(f"tahun : {data_waktu.year}")
print(f"hari : {data_waktu.strftime('%A')}")

from collections import Counter

data = [2,6,8,9,1,4,2,0,0,2,5,6,9,7,4]

dataCount=Counter(data)
print(f"Data Count : {dataCount}")
print(f"Jmlah data 5 = {dataCount[5]}")


import io
file=io.open("file_text.txt","r")
print(file.read())