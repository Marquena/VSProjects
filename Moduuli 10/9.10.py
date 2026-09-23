import random

class auto():
    def __init__(self,rek,maxvel,currvel,distance):
        self.rek = rek
        self.maxvel = maxvel
        self.currvel = currvel
        self.distance = distance

    def kiihdytä(self, muutos):
        if self.currvel + muutos > 0:
            if self.currvel + muutos < self.maxvel:
                self.currvel +=muutos
            else:
                self.currvel = self.maxvel
        else:
            self.currvel = 0
        return self.currvel
    def kulje(self,tunti):
        self.distance += self.currvel*tunti
        return self.distance

class kilpailu():
    def __init__(self, nimi, pit):
        self.nimi = nimi
        self.pit = pit
        self.auli = []
        for i in range(10):
            aa = auto(f"ABC-{i+1}",random.randint(100,200),0,0)
            self.auli.append(aa)
    def tulosta(self):
        for aa in self.auli:
            print(f"{aa.rek}\nMaksiminopeus: {aa.maxvel}\nTämänhetkinen nopeus: {aa.currvel}\nKuljettu Matka: {aa.distance}\n")
        print("\n-------------------------------------")
    def yh(self):
            for aa in self.auli:
                aa.kiihdytä(random.randint(-10,15))
                aa.kulje(1)
    def maali(self):
        lp = True
        while lp:
            for i in range(10):
                if lp== False:
                    break
                kilpailu.yh(self)
                for aa in self.auli:
                    if aa.distance>self.pit:
                        lp = False
                        break
                i+=1
                kilpailu.tulosta(self)
            kilpailu.tulosta(self)

kk = kilpailu("Suuri romuralli",8000)
kk.maali()
print(f"Tämä oli "+kk.nimi+", tervetuloa uudestaan")