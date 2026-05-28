print("Program powinien odwrócić kolejność cyfr w liczbie.")
while True:
    liczba = int(input("Liczba:" ))
    calosc = 0
    while liczba > 0:
        cyfra = liczba % 10
        calosc = calosc * 10 + cyfra
        liczba = liczba //10
    print(calosc)
