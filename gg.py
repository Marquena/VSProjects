import json
class obj():
    def __ini__(self, name, weight, cpst):
        self.name = name
        self.weight = weight
        self.cpst = cpst
class pelaaja():
    def __init__(self,name,age,phase,lvl,inv):
        self.name = name
        self.age=age
        self.phase = phase
        self.lvl = lvl
        self.inv=inv

def TR():
    return False

a = pelaaja
a.name = "aaa"
a.age = 3
a.phase = 0
a.lvl = 0
a.inv = []

miekka = obj
miekka.name="Miekka"
miekka.weight = 12
miekka.cpst = 5000

ab = {"name":miekka.name,
      "paino":miekka.weight,
      "hinta":miekka.cpst}

lapio = obj
lapio.name = "lapio"
lapio.weight = 2
lapio.cpst = 10
bb = {"name":lapio.name,
      "paino":lapio.weight,
      "hinta":lapio.cpst}

a.inv.append(ab)
a.inv.append(bb)

save_data = {"pelaaja": a.name,
        "ika":a.age,
        "phase":a.phase,
        "lvl": a.lvl,
        "inv":a.inv}


print(a)
with open("C:/Users/milop/.vscode/VSProjects/test.json","w")as save:
    json.dump(save_data, save)
with open("C:/Users/milop/.vscode/VSProjects/test.json","r")as save:
    ac = json.load(save)
del (ac["inv"][1])

with open("C:/Users/milop/.vscode/VSProjects/test.json","w")as save:
    json.dump(ac, save)
for item in ac["inv"]:
    if item["nimi"] == "miekka":
        print(item)


