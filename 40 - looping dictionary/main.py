# Loopig dictionary
# bisa mengambil 1. key saja, 2. values saja, 3.key dan values, 4.key dan values dalam 1 looping


data_dict={
    "cup" :"Ucup surucup",
    "tong": "Otong surotong",
    "dung" : "dudung surudung",
    "raha": "Rahadian Santoso"
}

# 1. looping first try
# yang keluar key-nya aja
for teman in data_dict:
    print(teman)

#Operator yang mengambil item /iterables
keys = data_dict.keys()
print(keys)

## mengambil value dari data dict (cara 1)
for element in data_dict:
    print(data_dict.get(element))

##mengambil data interebales bentuknya (cara 2)(['Ucup surucup', 'Otong surotong', 'dudung surudung', 'Rahadian Santoso'])

#mengambil values-nya
values=data_dict.values()
print(values)
for element in data_dict.values():
    print(element)

#mengambil itemnya
items=data_dict.items()
print(items)

for element in data_dict.items():
    print (element)


for key,values in data_dict.items():
    print(f"ini {key}, ini value {values}")