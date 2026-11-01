def bencon(määrä):
    return määrä*3.735

while True:
    ip = float(input("Anna gallonamäärä: "))
    if ip <0:
        break
    else:
        print("Litroina: ", bencon(ip))
    
