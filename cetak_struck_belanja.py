# by : Tri Yoga Dimas Syahputra
# description : mencetak bon belanja atau stuck belanja
# function : ketika user membeli suatu produk dan menginput jumlah yang ingin dibeli,
#            maka akan tercetak ke layar struk belanja

produk=['Indomie','Milo','Baterai','Sunslik','Aqua'] # terdapat beberapa list pada variable produk
print(57*"`")
print("- Berikut daftar makanan yang tersedia di Warung Python -")
print(57*"`")

harga=produk[:]           # copy list dari variable produk ke variabel harga
harga[0]=2500             # ubah Indomie jadi seharga 2500
harga[1]=4000             # ubah Milo jadi seharga 4000
harga[2]=1500             # ubah Baterai jadi seharga 1500
harga[3]=1000             # ubah Sunslik jadi seharga 1000
harga[4]=4500             # ubah Agua jadi seharga 4500
i=0                       # inisialisasi nilai i=0

for p in produk:                         # for / selama ada produk yang terdapat pada list
    print(i,'.', p, ': Rp. ', harga[i],',-') # cetak ke layar (string dan int)
    i+=1                                 # inisialisasi pertambahan nilai i ditambah 1

print('\nHint : untuk membeli Milo maka masukkan indeksnya = 1')    # cetak contoh pengisian nilai atau value
print('Hint : untuk membelinya banyaknya maka masukkan jumlahnya = 5')    # cetak contoh pengisian nilai atau value
beli=int(input("\nMasukkan nomor indeks yang ingin anda beli : "))       # variable beli sebagai input bertipe int

if beli >= 0 and beli <= 4:         #jika indeks = 1 sampai 4 maka truem selain itu maka false

    jumlah_beli = int(input("\nMasukkan jumlah yang ingin anda beli : "))  # variable jumlah_beli sebagai input

    total_harga = harga[beli] * jumlah_beli         # variable total_harga digunakan untuk menghitung harga

    print('Total harga yang harus anda bayar ialah : Rp.', total_harga, ',-')   # cetak ke layar bahwa indeks salah

    uang_cash=int(input('Masukkan jumlah uang yang anda gunakan untuk membayar : '))  # input pada variable uang_cash
    kembalian=uang_cash-total_harga             # pengurangan untuk menghitung uang kembalian pada variable kembalian

    print('Total kembalian dari uang anda adalah : Rp.', kembalian, ',-')   # cetak string dan nilai dari kembalian

    print('\nproses cetak struk belanja...\n')    # cetak ke layar dengan break menggunakan \n

    print(33*'-')
    print(9*'-','Warung Online',9*'-')
    print('-',produk[beli],' : Rp.',harga[beli],',-')
    print('- Jumlah Beli :', jumlah_beli,' Pcs')
    print('- Total Harga : Rp.', total_harga,',-')
    print('- Uang Cash : Rp.', uang_cash,',-')
    print('- Kembalian : Rp. ', kembalian,',-')
    print(33 * '-')
    print('| ^-_-^ Happy Shopping... :D |')
    print(33 * '-')

else:
    print('Maaf indeks produk yang anda masukkan salah')                        # cetak ke layar bahwa indeks salah