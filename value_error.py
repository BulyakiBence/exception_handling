
try:
    szam = int(input("Adj meg egy számot: "))
    print(f"A szám négyzete: {szam**3}")
except ValueError:
    print("Nem számot adtál meg")
