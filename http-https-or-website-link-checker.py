# by : Tri Yoga Dimas Syahputra
# name of the code : Website link Checker
# description : mengecek atau memvalidasi apakah link yang dimasukkan valid atau tidak.
# function : - mengecek apakah terdapat tulisan http:// atau https:// pada link web yang di input
#            - mengecek apakah terdapat tulisan .com pada akhir teks atau 2 atau 3 karakter dibelakang '.'

print('\n*******************************') #cetak kelayar dengan break '\n'
print('*Welcome to Link Validator App*') #cetak kelayar'
print('*******************************\n') #cetak kelayar dengan break '\n'

link=input('Please, input a website link : ') #masukkan website ke variable link

if link[0:7] == 'http://' or link[0:8] == 'https://' and link[-4] == '.' or link[-3] == '.': #jika kondisi ini bernilai true
        print('Your website link is valid') #cetak kelayar'
else:
        print('Your website link is not valid') #cetak kelayar'
        print('Please use http:// or https:// in the first link and make sure that your top level domain is correct') #cetak kelayar'
        print('Hint : http://yourdomain.com') #cetak kelayar'
