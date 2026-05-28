while True:
    liczba = int(input("Podaj liczbę: "))
    n = 1
    potega = 2
    while True:
        if potega <= liczba:
            n = n + 1
            potega = 2 ** n
        else:
            n = n - 1
            potega = 2 ** n
            break

    print(potega)

