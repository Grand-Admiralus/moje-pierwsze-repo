liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

if liczba1 >= liczba2:
    if liczba1 == liczba2:
        print("Liczby są równe.")
    else:
        print("Pierwsza liczba jest większa od drugiej.")
else:
    print("Pierwsza liczba jest mniejsza od drugiej.")