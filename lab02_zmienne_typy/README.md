# Lab 02 – Zmienne, typy danych i operacje arytmetyczne

📅 wtorek 13.10.2026, 08:30–11:45 · 📍 sala A/121 · ⏱ 4 h
**Sylabus:** treść nr 4 · **Efekty:** U1, U3, KS1 · **Slajdy:** [slajdy.md](slajdy.md)

## Cel zajęć

Po zajęciach potrafisz:
- używać typów `int`, `float`, `str` i konwertować między nimi,
- stosować operatory `+ - * / // % **`,
- pisać programy przeliczające jednostki,
- formatować liczby w f-stringach.

## Na start: fork i Lab 01

**Nie masz jeszcze forka?** Zrób go teraz według [SETUP.md](../SETUP.md), krok 4: **Fork** → włącz **Actions** → sklonuj **swój** fork.

**Sklonowałeś repozytorium prowadzącego bez forka?** Zrób fork, a potem w terminalu (wstaw swój login):

```bash
git remote set-url origin https://github.com/TWOJ_LOGIN/KU-PyDev.git
git pull --no-rebase --no-edit
```

**Masz już fork?** Na GitHubie kliknij **Sync fork → Update branch**, a potem `git pull`.

> 📌 **Dziś oddajesz też Lab 01.** Zacznij od zadań ★ w [`lab01_podstawy`](../lab01_podstawy/) (jeśli masz je zrobione – wystarczy push), potem przejdź do Lab 02.

## Zadania obowiązkowe ★

| Plik | Zadanie | Czas |
|---|---|---|
| `zad1_kalkulator.py` | Wynik 7 działań na dwóch liczbach | 30 min |
| `zad2_temperatura.py` | °C → °F i °F → °C | 30 min |
| `zad3_waluty.py` | PLN → EUR i USD (kursy stałe) | 30 min |
| `zad4_czas.py` | Sekundy → `h min s` (`//` i `%`) | 40 min |

## Zadania dodatkowe ☆

| Plik | Zadanie |
|---|---|
| `zad5_fibonacci.py` | n pierwszych wyrazów ciągu Fibonacciego (zapowiedź pętli `for`) |

## Jak sprawdzić rozwiązanie

W folderze `lab02_zmienne_typy`:

```bash
python -m unittest discover -s tests -v
```

> Format wyjścia w `zad4_czas.py` musi być **dokładnie** taki: `1 h 2 min 5 s`.

## Oddanie

Do **11:45** (z głównego folderu repozytorium):

```bash
git add lab01_podstawy lab02_zmienne_typy
git commit -m "Lab 01 i Lab 02"
git push
```

Jeden push przed 11:45 wystarczy na oba punkty – testy w Actions sprawdzają wszystkie laby naraz.

> ℹ️ Czerwony ❌ przy całym uruchomieniu w zakładce **Actions** jest normalny – laby, których jeszcze nie było, nie przechodzą testów. Otwórz uruchomienie i sprawdź zadania **`testy (lab01_podstawy)`** i **`testy (lab02_zmienne_typy)`** – te muszą być zielone ✅.

> ⏰ **Punkt za aktywność tylko za push przed 11:45** – liczy się godzina na GitHubie (zakładka Actions), nie data commita. Po zajęciach, nawet minutę później, punktu już nie ma. Nieobecność = brak punktu. Wymagane: wszystkie testy ★ zielone. [Zasady](../README.md#punkty-za-aktywność--tylko-za-pracę-na-zajęciach)

## Do poczytania

- E. Matthes, *Python. Instrukcje dla programisty* – rozdz. 2
- M. Dawson, *Python dla każdego* – rozdz. 2
