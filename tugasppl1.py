#Buat 3 objek ['Agama', 'Islam' , 'kristen']
#Agama = kelas induk
#Islam,kristen = kelas turunan

class Agama:
    def __init__(self,nama,agama):
        self.nama = nama
        self.agama = agama
        
    def perkenalan(self):
        print("Halo nama saya", self.nama,"agama saya", self.agama)
        
class Islam(Agama):
    def __init__(self,nama,agama,beribadah):
        Agama.__init__(self, nama, agama)
        self.beribadah= beribadah
         
class Kristen(Agama):
    def __init__(self,nama,agama,beribadah):
        Agama.__init__(self, nama, agama)
        self.beribadah= beribadah

Hisyam = Islam('Hisyam', 'Islam', 'Sholat')
Hisyam.perkenalan()
print(f'Saya beribadah dengan melakukan {Hisyam.beribadah}\n')

Abraham = Kristen('Abraham', 'Kristen', 'Sembahyang')
Abraham.perkenalan()
print(f'Saya beribadah dengan melakukan {Abraham.beribadah}')