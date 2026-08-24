import math

luoti = 13.3
naula = luoti*32
lieviskä = naula*20

lievin = float(input("Anna lievisköjen määrä: "))
naulain = float(input("Anna naulojen määrä: "))
luotiin = float(input("anna luotien määrä: "))

lievfin = lieviskä * lievin
naulafin = naulain * naula
luotifin = luotiin * luoti

täys = lievfin + naulafin + luotifin
gram, kilo = math.modf(täys/1000)

print("Kokonaispaino moderneilla mittayksiköillä on: ")

print(f"{kilo:10.0f}", " Kilogrammaa")
print(f"{gram*1000:10.1f}"," Grammaa")
