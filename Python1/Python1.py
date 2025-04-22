
liczba1 = float(input("Podaj pierwsza liczbe: "))
liczba2 = float(input("Podaj druga liczbe: "))
dzialanie = input("Wybierz dzialanie (+, -, * lub /): ")

if dzialanie == "+":
    wynik = liczba1 + liczba2
elif dzialanie == "-":
    wynik = liczba1 - liczba2
elif dzialanie == "*":
    wynik = liczba1 * liczba2
elif dzialanie == "/":
    if liczba2 != 0:
        wynik = liczba1 / liczba2
    else:
        wynik = "Blad: Dzielenie przez zero!"
else:
    wynik = "Nieznana operacja!"

print("Wynik:", wynik)
