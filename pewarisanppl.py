class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
        
    def perkenalan(self):
        print("Halo nama saya", self.nama,"dari", self.asal)
 
class Pelajar(Orang):
    def __init__(self, nama, asal, sekolah):
        Orang.__init__(self, nama, asal)
        self.sekolah= sekolah
    
class Pekerja(Orang):
    def __init__(self,nama, asal, kantor):
        super().__init__(nama, asal)
        self.kantor= kantor
       
stella = Orang('Stella','Jakarta\n')
stella.perkenalan()

ananta = Pelajar('Ananta','Bandung', 'SMKJP1')
ananta.perkenalan()
print(f'Saya Sekolah di{ananta.sekolah}\n')

Zayn = Pekerja('Zayn','Surabaya', 'PT.Smartschool')
Zayn.perkenalan()
print(f'Saya Kerja di{Zayn.kantor}')