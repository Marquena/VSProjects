import random
noppa = 0
määrä = int(input("Kuinka monta noppaa haluat heittää?: "))

for i in range(määrä):
    noppa += random.randint(1,6)
print(noppa)
