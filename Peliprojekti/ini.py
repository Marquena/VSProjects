
class obj():
    def __init__(self,nimi,paino,hinta):
        self.nimi = nimi
        self.paino = paino
        self.hinta = hinta

class huone():
    def __init__(self,nimi,esine):
        self.nimi=nimi
        self.nimi=esine
class pelaaja():
    def __init__(self,name,age,phase,lvl,inv):
        self.name = name
        self.age=age
        self.phase = phase
        self.lvl = lvl
        self.inv=inv

i1 = obj
i1.nimi = "Miekka"
i1.paino = 4
i1.hinta = 500
miekka = {"nimi":i1.nimi,
          "paino":i1.paino,
          "hinta":i1.hinta}

i2 = obj
i2.nimi = "lapio"
i2.paino = 2
i2.hinta = 10
lapio = {"nimi":i2.nimi,
          "paino":i2.paino,
          "hinta":i2.hinta}
i3 = obj
i3.nimi = "kalapussi"
i3.paino = 1
i3.hinta = 5
kalapussi = {"nimi":i2.nimi,
          "paino":i2.paino,
          "hinta":i2.hinta}

