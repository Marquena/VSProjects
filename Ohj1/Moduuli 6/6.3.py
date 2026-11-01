luku = int(input("Anna luku: "))

alk=True
for jako in range(2, luku):
    if luku % jako == 0:
        alk = False
        break
if alk:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")