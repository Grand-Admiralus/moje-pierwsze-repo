poprawna = 7

odp = int(input("Podaj ilość dni w tygodniu: "))

if odp == poprawna:
    print("Poprawna odpowiedź")
else:
    print("Błędna odpowiedź. Druga próba.")
    odp2 = int(input("Podaj ilość dni w tygodniu: "))
    if odp2 == poprawna:
        print("Poprawna odpowiedź")
    else:
        print("Błędna odpowiedź")