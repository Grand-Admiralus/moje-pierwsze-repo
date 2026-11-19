n = int(input("Podaj dodatnią liczbę całkowitą: "))

if n < 0:
    print("Błąd! Podaj liczbę dodatnią!")
elif n == 1:
    pass
else:
    for i in range(1, n+1):
        if i%2 == 0:
            print(i)
        else:
            pass