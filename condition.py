'''
percabangan (conditional statement)
percabangan merupakan suatu struktur yang memungkinkan program
dalam membuat keputusan berdasarkan kondisi yang telah diatur
'''

# percabangan tunggal
x = 20
if x > 50:
    print ('x lebih besar dari 50')

# percabangan ganda (if - else)
data = 20

if data == 20:
    print ('benar')
else : 
    print ('salah')


# percabangan berantai (if - elif - else) 
angka = int (input ('masukkan angka : '))

if angka > 50:
    print ('benar')
elif angka < 50:
    print ('salah')
else :
    print ('selesai')

# percabangan bersarang
x = 25

if x > 10: # x lebih besar dari 10
    if x < 50: # x lebih kecil dari 50
        print("x berada di antara 10 dan 50")


    