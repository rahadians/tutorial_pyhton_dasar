'''Type hints untuk fungsi'''

#bentuk standart fungsi yang kita pelajari

# kesalahan pembuatan parameter input any karena beda type data bisa error
'''
def fungsi(parameter):
    print(parameter)

fungsi(1)
'''


# penggunaan type hints
# ->int adalah outputnya
import string


def fungsi_dengan_hints(argument:int)->int:
    '''Fungsi dengan hints'''
    output= 10**argument
    return output

hasil=fungsi_dengan_hints(3.3)
print(hasil)


def display(argument:string)->string :
    print(argument)

display("string harus diimport terlebih dahulu")

display(2)
