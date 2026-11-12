punkty = int(input("Podaj ilość punktów: "))

if punkty >= 10:
    print("Zaliczone!")
else:
    brakuje = 10 - punkty
    print("Niezaliczone.")
    print(f"Brakuje punktów: {brakuje}")