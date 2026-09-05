import random

N = int(input("Anna arvottavien pisteiden määrä: "))
n = 0

for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        n += 1

likia = 4 * n/N
print("Piin likiarvo on", likia)