n = int(input("Podaj ilość liczb. "))
x = 0
proba = 1

for i in range(1, n+1):
    x = int(input(f"Podaj kwadrat liczby {i}: "))
    while proba != 3:
        if x != i**2:
            print("Błędna odpowiedź! Spróbuj jeszcze raz!")
            x = int(input(f"Podaj kwadrat liczby {i}: "))
            proba = proba+1
        else:
            print("Poprawna odpowiedź!")
            proba = 1
       