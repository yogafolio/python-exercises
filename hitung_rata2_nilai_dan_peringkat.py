#dalam penghitungan nilai rata" ini menggunakan beberapa mata pelajaran
mapel=["Biologi", "Kimia", "Matematika", "Sosiologi", "Geografi", "Fisika"] # data list
nilai=mapel[:]                                                              # copy dari data list variable mapel

print(nilai[0])                                    # print list pertama
nilai[0]=input("Masukkan Nilai : ")                # input list pertama

print(nilai[1])                                     # print list kedua
nilai[1]=input("Masukkan Nilai : ")                 # print list kedua

print(nilai[2])                                     # data print list ketiga
nilai[2]=input("Masukkan Nilai : ")                 # print list ketiga

print(nilai[3])                                     # data print list keempat
nilai[3]=input("Masukkan Nilai : ")                 # print list keempat

print(nilai[4])                                     # data print list kelima
nilai[4]=input("Masukkan Nilai : ")                 # print list kelima

print(nilai[5])                                     # data print list keenam
nilai[5]=input("Masukkan Nilai : ")                 # print list keenam

total=int(nilai[0])+int(nilai[1])+int(nilai[2])+int(nilai[3])+int(nilai[4])+int(nilai[5]) # hitung total nilai
rata2=total//len(mapel)                              # hitung rata-rata

print("\nNilai rata-rata anda adalah : ", rata2)     #print nilai rata-rata

if rata2 >= 0 and rata2 <= 20 :                             # jika rata-rata 0 sampai 20
    print("Peringkat yang anda dapatkan adalah : E")        # print peringkat E
elif rata2 >= 21 and rata2 <= 40 :                          # jika rata-rata 21 sampai 40
    print("Peringkat yang anda dapatkan adalah : D")        # print peringkat D
elif rata2 >= 41 and rata2 <= 60 :                          # jika rata-rata 41 sampai 60
    print("Peringkat yang anda dapatkan adalah : C")        # print peringkat C
elif rata2 >= 61 and rata2 <= 80 :                          # jika rata-rata 61 sampai 80
    print("Peringkat yang anda dapatkan adalah : B")        # print peringkat B
elif rata2 >= 81 and rata2 <= 100:                          # jika rata-rata 81 sampai 100
    print("Peringkat yang anda dapatkan adalah : A")        # print peringkat A
else:
    print("Nilai anda diluar antara 1 - 100")               # print nilai diluar jangkauan

# by : Tri Yoga Dimas Syahputra