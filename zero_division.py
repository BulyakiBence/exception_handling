try:
    osztando = 10
    oszto = int(input(f"Mennyivel osszam el a {osztando}-es számot? "))
    print(f"A két számn hányadosa: {osztando/oszto}")
except ZeroDivisionError:
    print("Nullával nem osztunk")