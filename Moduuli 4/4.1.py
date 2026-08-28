pituus = float(input("Kuhan pituus senttimetreinä: "))
if pituus <37:
    print(f"kuha on {37-pituus:2.1f} senttiä liian lyhyt. Päästä takaisin")
else:
    print("voit pitää kuhan jipii")