import math

def suhde(halk, hinta):
    ar = (halk/2)*math.pi**2
    return ar/hinta

ha = float(input("Kerro pitsan halkaisija senttimetreinä: "))
hi = float(input("kerro pitsan hinta euroina: "))
p1 = suhde(ha, hi)

ha = float(input("Kerro toisen pitsan halkaisija senttimetreinä: "))
hi = float(input("kerro toisen pitsan hinta euroina: "))
p2 = suhde(ha, hi)

if p1>p2:
    print("pitsa 1 antaa enemmän pitsaa per euro")
elif p2>p1:
    print("pitsa 2 antaa enemmän pitsaa per euro")
else:
    print("molemmat antaa saman verran")