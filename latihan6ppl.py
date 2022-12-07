# jenis enkapsulasi : public,protected, private

# Membuat public class 

class segitiga :
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0,5 * alas * tinggi;
        
#instansiasi
segitiga_besar = segitiga(100, 80)

#print
print('ini adalah public class')
print(f'Alas : {segitiga_besar.alas}')
print(f'Tinggi : {segitiga_besar.tinggi}')
print(f'Luas : {segitiga_besar.luas}\n')

#Membuat protected class
#memakai 1 _
class mobil: #class induk
    def __init__(self,merk):
        self._merk = merk  #protected class declaration
        
class mobilefwan(mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk) #panggil merk dibagian sini
        self._total_gear = total_gear
        
    def pamer(self):
        #hak akses _merk dari subclass/class turunan
        print (f'ini adalah mobil {self._merk} dengan total gearnya {self._total_gear}\n')
            
#instansiasi 
print('ini adalah protected class')
ferrari = mobilefwan('ferrari ', 8)
ferrari.pamer()

#membuat private class
#memakai 2 __
class motor:
    def __init__(self, merk):
        self.__merk = merk #private class declaration
        
    def tampilkan_merk(self):
        print(f'Merk motornya : {self.__merk}')
        #panggil private disini(harus satu class gabisa dipanggil diluar class/gabisa ke class lain)
            
        
#instansiasi
print('Ini adalah private class')
moge = motor('Harley')
moge.tampilkan_merk()