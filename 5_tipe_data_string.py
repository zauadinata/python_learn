# string
print ('hello world') # 1 tanda petik
print ("hello world") # 2 tanda petik

# string dan memanipulasinya

# menambahkan variabel yang di dalamnya terdapat format string
nama = 'adinata'
str = 'hello ' + nama
print (str)

# konstruksi dengan format string
data = 'adinata'
format_str = f'halo {data}'
print (format_str)

# penggunaan angka 
tahun = 2024
format = f'tahun : {tahun}'
print (format)

# memanipulasi angka dengan koma sebagai batas
angka = 5000
data = f'angka : {angka:,}'
print (data)

# bilangan dengan menampilkan data setelah koma
angka = 20.123456
data = f'angka : {angka:.2f}'
print (data)

# memformat persen
persen = 0.9080
data = f'persen : {persen:.2%}'
print (data)

# multiline string
nama = 'adinata'
lahir = 2004

data = f"""
nama = {nama}
lahir = {lahir}
"""
print (data)

# mengatur lebar
nama = 'adinata'
lahir = 2004

data = f"""
nama    = {nama:>20}
lahir   = {lahir}
"""
print (data)
