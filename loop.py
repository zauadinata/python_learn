'''
loop atau perulangan terbagi menjadi 2,
yaitu menggunakan perintah 'for' dan 'while'
'''

# penggunaan for digunakan untuk mengiterasi elemen-elemen dalam sebuah koleksi atau rentang yang telah ditentukan

# program akan menampilkan angka sebanyak 5 kali dimulai dari 0
data = 5
for i in range (data):
    print (i)

# for dengan list
data_list = [1,2,3,4,5]
for i in (data_list):
    print (i)

# mengetahui cara kerja for
# apel di dalam list menunjukkan urutan ke 0 karena dimulai dengan index
buah = ["apel", "pisang", "jeruk"]

for index, fruit in enumerate(buah):
    print(f"Index {index}: {fruit}")


# penggunaan while digunakan untuk mengulang blok kode selama suatu kondisi bernilai True atau benar
# while dasar
count = 1 # dimulai dari 1
while count <= 5: 
    print (f'angka : {count}')
    count += 1

# while dengan mengulang sehingga mendapatkan hasil yang ditentukan
while True :
    kondisi =  (input ('ya atau tidak : '))
    if kondisi == 'ya':
        print ('selesai')
        break
    else :
        print ('lanjut')

# pola while
while True :
    print ('tak hingga')
# pada dasarnya jika program while hanya seperti di atas
# maka output nya akan terus mengulang tiada henti

