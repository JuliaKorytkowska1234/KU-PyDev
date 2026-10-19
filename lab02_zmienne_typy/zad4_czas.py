# Lab 02 – Zadanie 4 (★): Sekundy na godziny, minuty i sekundy
#
# Program wczytuje liczbę sekund (int) i wypisuje ją DOKŁADNIE w formacie:
#     1 h 2 min 5 s
# (dla 3725 sekund).
#
# Wskazówki:
#   - int(input(...)) – konwersja tekstu na liczbę całkowitą
#   - // dzielenie całkowite, % reszta z dzielenia
#   - 1 h = 3600 s, 1 min = 60 s

# TODO: Twój kod poniżej
sekundy = int(input("Podaj liczbę sekund "))
godz = sekundy // 3600
min = (sekundy / 60) % 60
sek = (sekundy % 3600) // 60
print(f"{godz:.0f} h {min:.0f} min {sek:.0f} sek")
