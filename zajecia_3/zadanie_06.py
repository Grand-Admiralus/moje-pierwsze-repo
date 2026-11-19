print("Podaj liczby do sumowania. Wpisz 0 gdy chcesz zakończyć program.")

suma = 0
n = 1
repetycje = 0

while n != 0:
    n = int(input("Podaj swoją liczbę: "))
    suma = suma + n
    repetycje = repetycje + 1

print(f"Suma: {suma}")
print(f"Liczba wartości: {repetycje-1}")