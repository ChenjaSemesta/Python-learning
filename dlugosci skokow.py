maks = 0

a = float(input("""Podaj długości poszczególnych skoków w metrach, wpisz "0", aby zakończyć liste:
"""))

while a != 0:
    if a > maks:
        maks = a
print("\nNajdłuższy skok to: ", maks, "m")
