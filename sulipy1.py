"""
1. Feladat
Írj egy programot, ami a felhasználótól három egész számot számot kér be egyesével, ezeket eltárolja egy listában, majd a képernyőre kiírja a lista tartalmát! Ha a felhasználó nem számot ad meg, kapjon hibaüzenetet, és ismétlődjön meg a bekérés!

"""
# szamok = []
# while True:
#     try:
#         szam1 = int(input("Adj meg egy számot: "))
#         szam2 = int(input("Adj meg egy számot: "))
#         szam3 = int(input("Adj meg egy számot: "))   

#         szamok.append(szam1) 
#         szamok.append(szam2)
#         szamok.append(szam3)  

#         print(f"A számok: {szamok}")
#         break
#     except ValueError as e:
#         print(e)
#         print("Nem számot adtál meg")

szamok = []
for i in range(3):
    while True:
        try:
            szam = int(input(f"{i+1}. szám: "))
            szamok.append(szam)
            break
        except ValueError as e:
            print(e)
            print("Nem számot adtál meg")

print(f"A lista tartalma: {szamok}")            