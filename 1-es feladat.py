osztando = 10
while True:
    
    try:
        oszto = int(input(f"Mennyivel osszam el a {osztando}-es számot? "))
        print(f"A két számn hányadosa: {osztando/oszto}")
        break
    except ZeroDivisionError:
        print(e)
        print(" ZeroDivisionError: Nullával nem osztunk")
    except ValueError as e:
        print(e)
        print("ValueError: Nem számot adtál meg")    