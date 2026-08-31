import random
def noppa(sivu):
    return random.randint(1, sivu)
    
sivin = int(input("Kuinka monta sivuista noppaa haluat heittää?: "))

while True:
    ab=noppa(sivin)
    print(ab)
    if ab == sivin:
        break