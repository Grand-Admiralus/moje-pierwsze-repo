n = int(input("Podaj liczbę studentów: "))
suma = 0
wynik = 0

for i in range(1, n+1):
    wynik = int(input(f"Podaj wynik studenta nr. {i}: "))
    while wynik not in range(0,101):
        print("Niepoprawny wynik!")
        wynik = int(input(f"Podaj wynik studenta nr. {i}: "))
    suma = suma+wynik

print(f"Suma: {suma}")
    