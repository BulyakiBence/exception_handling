osztando = 10
try:
    oszto = int(input(f"Mennyivel osszam el a {osztando}-es számot? "))
    print(f"A két számn hányadosa: {osztando/oszto}")
except ZeroDivisionError as e:
    print(e)
    print(" ZeroDivisionError: Nullával nem osztunk")
except ValueError as e:
    print(e)
    print("ValueError: Nem számot adtál meg")