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
autot = []
for i in range(10):
    aa = auto(f"ABC-{i+1}",random.randint(100,200),0,0)
    autot.append(aa)
lp = True
while lp:
    for aa in autot:
        aa.kiihdytä(random.randint(-10,15))
        aa.kulje(1)
    for aa in autot:
        if aa.distance>10000:
            lp=False
            break
for aa in autot:
    print(f"{aa.rek}\nMaksiminopeus: {aa.maxvel}\nTämänhetkinen nopeus: {aa.currvel}\nKuljettu Matka: {aa.distance}\n")