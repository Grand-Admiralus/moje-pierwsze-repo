n = int(input("Podaj nieujemną liczbę całkowitą: "))

if n < 0:
    print("Błąd! Podaj liczbę nieujemną!")
elif n == 1:
    print("Python 0")
else:
    print("Python 0")
    i = 1
    while i < n:
        print(f"Python {2**i}")
        i = i+1