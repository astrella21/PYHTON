# membuat variabel atau box bernama buah
buah = ["apel", "durian", "kiwi", "alpukat", "mangga"]
sayur = ["pokcoy", "seledri", "kangkung", "bayem", "asem"]

#tampilkan data yang ada divariabel buah
#print (buah)

#tampilkan data berurutan dari awal hingga akhir
#for gerobak in buah:
#    print (gerobak)

#ditampilkan hanya beberapa data/buah saja
#print (buah[0],buah[2])

#untuk menambahkan data dipaling belakang
#buah.append("anggur merah")
#print (buah)

#cara menghapus yang ada di dalam buah
#buah.remove("kiwi")
#print (buah)

#cara memotong nilai yang ada di box buah
#print (buah[1:4])

#operasi aritmatika data list
#dagang_hari_ini = buah + sayur 
#print (dagang_hari_ini) 

#cara agar list kebawah
#for gerobak in dagang_hari_ini:
#    print (gerobak)
    
kasir = input("Mau tambah buah apa lagi? :")
buah.append(kasir)
print(buah)