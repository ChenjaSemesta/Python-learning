print("Sprawdzamy dzielniki liczby")

while True:
    liczba = int(input("Podaj liczbę, dla której sprawdziym możliwe dzielniki: "))
    dzielnik = liczba - 1
    while dzielnik > 0:
        wynik = liczba % dzielnik
        if wynik == 0:
            print(dzielnik, end=" ")
        dzielnik = dzielnik - 1

    print ()
