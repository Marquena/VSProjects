import random

num = random.randint(1, 10)
vast = 0
while vast !=num:
    vast = int(input("Arvaa numero 1-10: "))
    if vast <num:
        print("liian pieni vastaus")
    elif vast >num:
        print("liian suuri vastaus")
    else:
        print("oikea vastaus jipii")