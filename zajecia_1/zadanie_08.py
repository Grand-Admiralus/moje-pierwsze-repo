imie = input("Podaj swoje imię: ")
wynik1 = int(input("Podaj wynik pierwszej części testu: "))
wynik2 = int(input("Podaj wynik drugiej części testu: "))

suma = wynik1 + wynik2

if suma > 14 and wynik1 > 4 and wynik2 > 4:
    print(f"Student: {imie}")
    print(f"Suma: {suma}")
    print("Status: Zaliczone")
else:
    print(f"Student: {imie}")
    print(f"Suma: {suma}")
    print("Status: Niezaliczone")