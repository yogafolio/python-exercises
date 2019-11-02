print('-----------------------------------')                     #cetak ke layar
print("| SELAMAT DATANG DI PEMBUATAN ATM |")                     # tampilan awal ke user
print('-----------------------------------')                     #cetak ke layar

print('Untuk membuat rekening bank, anda memerlukan input beberapa data yang dibutuhkan') #cetak ke layar
namadepan=input('Masukkan nama depan anda : ')                       # input nama depan ke variable namadepan

namabelakang=input('masukkan nama belakang anda : ')                 # input nama belakang ke variable namabelakang

nik=input('masukkan NIK pada KTP anda : ')                           # input NIK ke variable nik

nohp=input('masukkan nomor handphone anda : ')                       # input NO HP ke variable nohp

email=input('Masukkan E-mail anda : ')                               #input email ke variable email

print('Note: Wajib 6 angka sebagai pin anda')                       #cetak ke layar

kali=['1','2','3']                                                  # trik mengakali untuk melakukan perulangan

pin=input('Masukkan Pin ATM anda : ')                                #cetak ke layar

if len(pin) is 6:                                                    #if jika penjang nilai variable pin = 6
    print('')                                                        #cetak ke layar
    print('Format pin benar\n')                                      #cetak ke layar
    print('Selamat! Akun rekening anda telah berhasil terdaftar')    #cetak ke layar
    print('----------------------------------------')                #cetak ke layar
    print('|Nama Lengkap :', namadepan, namabelakang, '|')           #cetak ke layar
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')                #cetak ke layar
    print('|NIK :', nik, '|')                                        #cetak ke layar
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')                #cetak ke layar
    print('|NO HP:', nohp, '|')                                      #cetak ke layar
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')                #cetak ke layar
    print('|E-mail', email, '|')                                     #cetak ke layar
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')                #cetak ke layar
    print('|pin anda adalah:', pin, '|')                             #cetak ke layar
    print('----------------------------------------')                #cetak ke layar
else:
    print('pin wajib terdiri dari 6 angka')                          #cetak ke layar
    pin = input('Masukkan Pin ATM anda : ')                           #input PIN ATM ke variable pin
    print('pin wajib terdiri dari 6 angka')                          #cetak ke layar
    for percobaan in kali :                                          #perulangan 3x
        pin = input('Masukkan Pin ATM anda : ')                       #input PIN ATM ke variable pin
        print('pin wajib terdiri dari 6 angka')                      #cetak ke layar
    else:
        print("Anda sudah mencoba 5 kali, maaf PIN anda tidak terdiri dari 6 angka") #cetak ke layar

# by : Tri Yoga Dimas Syahputra