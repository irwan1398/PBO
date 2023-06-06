class Manusia:
  # class attribute
  suku = "Jawa"
  
  def _init_(self, name, age, jnskel, agama, alamat, status):
    self.name   = nmae
    self.age    = age
    self.jnskel = jnskel
    self.agama  = agama
    self.alamat = alamat
    self.status = status
    
    def biodata(self):
      #return f"(self.name) is (self.age) yers old"
      return f"Nama: (self,name) \nUsia: (self.age) \nAgama: self(agama) \nJenis Kelamin: (self.jnskel) \nAlamat: (self.alamat) \nStatus: (self.status)'
    
    tes_Manusia = Manusia("Manusia","23","Agama","Laki-laki","Tegal","Jomblo")
    print(tes_Manusia.biodata())
