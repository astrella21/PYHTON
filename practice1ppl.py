#PRAKTEK ENKAPSULASI
#Buatlah masing2 parameter:
#Siswa - Public
#Guru - Protected
#Kepsek - Private

#Tampilkan
# 1. Siswa kami bernama Euroski
# 2. Guru kami bernama Bu Anita
# 3. Kepsek kami bernama Pak Lilik

#Public class
class Siswa:
    def __init__(self,Siswa):
        self.Siswa = Siswa
 
#instansiasi
Siswa_pelajar = Siswa('Euroski')       
   
#print   
print(f'Siswa kami bernama {Siswa_pelajar.Siswa}\n')  

#protected class
class Guru:
    def __init__(self,Guru):
        self._Guru = Guru
        
class Bu_Anita(Guru):
    def __init__(self,Guru):
        super().__init__(Guru)
        
    def Gurucantik(self):
        print(f'Guru kami bernama {self._Guru}\n')
        
#instansiasi
Bu_Guru = Bu_Anita('Anita')
Bu_Guru.Gurucantik()

class Kepsek:
    def __init__(self, Kepsek):
        self.__Kepsek = Kepsek
        
    def tampilkan_Kepsek(self):
        print(f'Kepsek kami bernama {self.__Kepsek}')
        
print 
cwo = Kepsek('Pak Lilik')
cwo.tampilkan_Kepsek()