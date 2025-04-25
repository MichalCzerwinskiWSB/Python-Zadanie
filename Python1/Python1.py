print("Wybierz program:")
print("1 - Kalkulator")
print("2 - Konwerter temperatur")
wybor = input("Twoj wybor (1/2): ")

if wybor == "1":
    print("\n--- Kalkulator ---")
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
            wynik = "Blad: Dzielenie przez zero"
    else:
        wynik = "Nieprawidlowa operacja"

    print("Wynik:", wynik)

elif wybor == "2":
    print("\n--- Konwerter temperatur ---")
    kierunek = input("Wybierz kierunek konwersji\n 1 - Celsjusz -> Fahrenheit,\n 2 - Fahrenheit -> Celsjusz: ")

    if kierunek == "1":
        temp_c = float(input("Podaj temperature w stopniach Celsjusza: "))
        temp_f = temp_c * 1.8 + 32
        print(f"{temp_c}C = {temp_f}F")

    elif kierunek == "2":
        temp_f = float(input("Podaj temperature w stopniach Fahrenheita: "))
        temp_c = (temp_f - 32) / 1.8
        print(f"{temp_f}F = {temp_c}C")

    else:
        print("Nieprawidlowa operacja.")

else:
    print("Nieznana opcja. Uruchom program ponownie.")
