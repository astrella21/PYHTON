#overloading: teknik di mana kita akan mengatur atau mendefinisikan perilaku sebuah kelas (yang kita buat), bagaimana ia akan berinteraksi dengan berbagai macam operator yang berbeda.

#Membuat Operator Overloading 
def garis():
    print ("-----------------")
class Angka:
    def __init__(self, angka):
        self.angka = angka
        
    def __add__(self, objek):
        return self.angka + objek.angka
    
x1 = Angka(17)
x2 = Angka(21)

print(x1 + x2)
garis()

#Menangani Operator Perbandingan
class Angka:
    def __init__(self, angka):
        self.angka = angka
    
    def __add__(self, objek):
        return self.angka + objek.angka
    
    def __mul__(self, objek):
        return self.angka * objek.angka
    
x1 = Angka(5)
x2 = Angka(12)
    
print(x1 + x2)
print(x1 * x2)