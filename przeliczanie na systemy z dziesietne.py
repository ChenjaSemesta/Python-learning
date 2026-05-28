print("Kalkulator zmieniający system zapisu liczby z dziesiętnego.")

while True:

    co = input("""Na jaki system liczbowy chcesz przeliczyć?
    Opcje:
    1. Binarny
    2. Szesnastkowy
    3. Ósemkowy
    4. Koniec
    Teraz możesz wpisywać: """).lower().strip()

    if co in ["4", "koniec", "k"]:
        print("Program kończy swoje działanie.")
        break

    dz = int(input("Podaj liczbę dziesiętną: "))

    if co in ["1", "binarny"]:
        print(dz, "w systemie binarnym to: ", bin(dz)[2:])
        continue

    elif co in ["2", "szesnastkowy"]:
        print(dz, "w systemie szesnastkowym to: ", hex(dz)[2:].upper())
        continue

    elif co in ["3", "ósemkowy", "oktalny"]:
        print(dz, "w systemie ósemkowym to: ", oct(dz)[2:])
        continue

    else:
        print("Polecenie nie jest na liście. Zaczynamy od początku.")
        continue
