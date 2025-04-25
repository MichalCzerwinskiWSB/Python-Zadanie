print("Wybierz program:")
print("1 - Kalkulator")
print("2 - Konwerter temperatur")
print("3 - Srednia ocen ucznia")
wybor = input("Twoj wybor (1/2/3): ")

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

elif wybor == "3":
    print("\n--- Srednia ocen ucznia ---")
    ilosc_ocen = int(input("Ile ocen chcesz wprowadzic? "))
    suma = 0

    for i in range(ilosc_ocen):
        ocena = float(input(f"Podaj ocene {i+1}: "))

        if ocena <= 6:
            suma += ocena
        else:
            print ("Blad: Ocena jest za wysoka. \n Podaj prawidlowa ocene: ")
            ocena = float(input(f"Podaj ocene {i+1}: "))
            suma += ocena

        
        

    srednia = suma / ilosc_ocen
    print(f"Srednia: {srednia:.2f}")

    if srednia >= 3.0:
        print("Uczen zdal.")
    else:
        print("Uczen nie zdal.")

else:
    print("Nieprawidlowa operacja.")
