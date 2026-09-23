class julk:
    def __init__(self,nimi,kirtoim,sivumäärä):
        self.nimi = nimi
        self.kirtoim = kirtoim
        self.sivumäärä = sivumäärä

class Kirja(julk):
    def ktulosta(self):
        print(self.nimi)
        print(self.kirtoim)
        print(self.sivumäärä)
class Lehti(julk):
    def ltulosta(self):
        print(self.nimi)
        print(self.kirtoim)


lehti = Lehti("Aku Ankka", "Aki Hyyppä",0)
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti.ltulosta()
kirja.ktulosta()

