import fun
import ini
import json

ss = input("Jos aikaisempia pelikertoja, syötä hahmon nimi\n>>> ")
with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","r") as save:
    data = json.load(save)
if ss in data["pelaaja"]:
    print("hahmo löytyi")
    input(">>> ")
else:
    fun.menu()

with open("C:/Users/milop/.vscode/VSProjects/Peliprojekti/save.json","r") as save:
    data = json.load(save)

ikä = data["ika"]
nimi = data["pelaaja"]
phase = data["phase"]
lvl = data["lvl"]
inv = data["inv"]

while True:
    #peli pyörii niin kauan että ohjelma suljetaan, joko häviöstä tai voitosta
    fun.peli(lvl,phase)
    lvl+=1
    phase = 0