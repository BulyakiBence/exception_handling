# I.
# Szimuláljuk egy 6 oldalú kocka 20 dobását! A dobásokat egy listában tároljuk!
# Majd oldjuk meg a következő feladatokat!
# Minden feladat előtt a program írja ki a feladat sorszámát!

# 1. Volt-e 6-ös dobás a listában?
# 2. Hanyadik dobás lett először 3-es?
# 3. Hány darab páros számot dobtunk?
# 4. Melyik volt a legkisebb dobás a 3-nél nagyobbak közül, és hányadik dobás volt?
# 5. Mennyi a 5-as dobások összege?
import random
dobasok = []
paros_szamok = []
negynel_nagyobb = []
otos_szamok = []
for i in range(21):
     i = random.randint(1,6)
     dobasok.append(i)
print(f"Dobásaid:{dobasok}")
print("-------------------/n")

print("1.feladat")
if 6 in dobasok:
    print("Volt benne 6-os")
else:
    print("Nem volt benne 6-os")

print("--------------------/n")

print("2es feladat")
if 3 in dobasok:
        index = dobasok.index(3)
        print(f"A {index + 1}. dobás lett 3-as")
else:
     print("Nem volt benne 3-as")        

print("3.feladat")
for szam in dobasok:
     if szam % 2 == 0:
      paros_szamok.append(szam)
if len(paros_szamok) > 0:
 print(f"Ennyi páros szám van benne: {len(paros_szamok)}")
else: 
    print("Nem volt páros")

print("4. feladat")
for szam in dobasok:
    if szam > 3:
      negynel_nagyobb.append(szam)
if len(negynel_nagyobb) > 0:
    print(f"A legkisebb 3nal nagyobb szam {min(negynel_nagyobb)}")
    print(f"Helye :{(dobasok.index(min(negynel_nagyobb)))+1}")
else:
    print("Nem volt 3-nál nagyobb")

print("-------------------/n")

print("5-ös feladat")
if 5 in dobasok:
    for szam in dobasok:
        if szam == 5:
            otos_szamok.append(szam)
    if len(otos_szamok) > 0:
        print(f"Ennyi ötös van benne {len(otos_szamok)}")
        otos_szamok_osszege = len(otos_szamok) * 5
        print(f"Összegük: {otos_szamok_osszege}")
        