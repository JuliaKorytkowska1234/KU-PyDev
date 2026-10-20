# Lab 03 – Zadanie 2 (★): Kalkulator z wyborem działania
#
# Program wczytuje kolejno: liczbę, operator (+, -, *, /) i drugą liczbę,
# a potem wypisuje wynik, np.:  8.0 * 2.0 = 16.0
#
# Obsłuż przypadki szczególne instrukcją if:
#   - dzielenie przez zero  -> "Nie można dzielić przez zero"
#   - inny operator         -> "Nieznany operator"

# TODO: Twój kod poniżej

liczba_1 = int(input("Podaj liczbe 1 "))
operator = input("Podaj operator ")
liczba_2 = int(input("Podaj liczbe 2 "))

if operator == "+":
    print(f"{liczba_1} + {liczba_2} = {liczba_1 + liczba_2}")

elif operator == "-":
    print(f"{liczba_1} - {liczba_2} = {liczba_1 - liczba_2}")

elif operator == "*":
    print(f"{liczba_1} * {liczba_2} = {liczba_1 * liczba_2}")

elif operator == "/":
    if liczba_2 == 0:
        print("Nie można dzielić przez zero")
    else:
      print(f"{liczba_1} / {liczba_2} = {liczba_1 / liczba_2}")

else:
    print("Nieznany operator")