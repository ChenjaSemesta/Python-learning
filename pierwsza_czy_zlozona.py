print("Kod sprawdza czy dana liczba jest pierwszą czy złożoną.")
while True:
    liczba = int(input("Podaj liczbę naturalną: "))
    dzielniki = 0
    for x in range(1, liczba+1):
        if (liczba % x) == 0:
            dzielniki += 1

    if dzielniki > 2:
        print("Ta liczba jest liczbą złożoną.")
    elif dzielniki == 2:
        print("Liczba jest liczbą pierwszą.")
    else:
        print("Ta liczba nie jest ani pierwszą ani złożoną.")

