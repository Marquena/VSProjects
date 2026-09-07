class hissi():
    def __init__(self, aker,yker):
        self.yker = yker
        self.aker = aker
        self.cker = aker

    def ylös(self):
            self.cker+=1
    def alas(self):
            self.cker-=1      
    def siirry(self,ker):
        if self.yker>=ker > self.cker:
            while ker>self.cker:
                self.ylös()
                print(self.cker)
        elif self.aker<=ker < self.cker:
            while ker<self.cker:
                self.alas()
                print(self.cker)
        elif ker == self.cker:
            print("olet jo tässä kerroksessa")
        else:
            print("Kerrosta ei olemassa")
        return self.cker
class talo():
    def __init__(self,aker,yker,hcount):
        self.hissit = []
        for i in range(hcount):
            self.hissit.append(hissi(aker,yker))

    def aja(self,hnum,kohde):
        h = self.hissit[hnum]
        h.siirry(kohde)

    def häl(self):
        print("HÄLYTYS")
        talo.aja(self,len(self.hissit)-1, 0)

        
        
lp=True

bb = talo(0, 10, 2)

bb.aja(0,4)
bb.aja(1,11)

bb.häl()

