import fun
import ini
import json

ss = input("Jos aikaisempia pelikertoja, syötä hahmon nimi\n>>> ")
with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","r") as save:
    data = json.load(save)
if ss in data["pelaaja"]:
    print("hahmo löytyi")
else:
    fun.menu()

with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","r") as save:
    data = json.load(save)
    
ikä = data["ika"]
nimi = data["pelaaja"]
phase = data["phase"]
lvl = data["lvl"]
inv = data["inv"]

fun.peli(data["lvl"],data["phase"])

print("voitit pelin yahhuuuu")


