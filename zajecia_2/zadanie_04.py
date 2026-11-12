liczba = int(input("Podaj swoją liczbę: "))

reszta = liczba%2

if liczba == 0:
    print("Zero nie jest ani parzyste, ani nieparzyste!")
else:
    if reszta == 0:
        print("Liczba jest parzysta!")
    else:
        print("Liczba jest nieparzysta!")