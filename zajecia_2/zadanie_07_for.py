n = int(input("Podaj nieujemną liczbę całkowitą: "))

if n < 0:
    print("Błąd! Podaj liczbę nieujemną!")
elif n == 0:
    pass
else:
    print("Python 0")
    for i in range(n-1):
        print(f"Python {2**(i+1)}")