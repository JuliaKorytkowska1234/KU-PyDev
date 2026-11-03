# Lab 04 – Zadanie 5 (☆, dodatkowe): Mini-crawler
#
# Crawler (robot sieciowy) przegląda strony i zbiera z nich linki.
# Przeczytaj plik dane/strona.html i:
#   1. policz wszystkie linki – wystąpienia tekstu  href="
#   2. wypisz domeny linków bez powtórzeń, np. docs.python.org
#
# Wynik:
#     Liczba linków: 5
#     www.python.org
#     docs.python.org
#     ...
#
# Wskazówki:
#   - text.find('href="', start) zwraca pozycję albo -1 – szukaj w pętli while
#   - adres kończy się na kolejnym znaku "
#   - domena to fragment między "://" a pierwszym "/" po nim
#   - (dla chętnych) urllib.request.urlopen pobierze prawdziwą stronę

with open("dane/strona.html", encoding="utf-8") as f:
    html = f.read()

# TODO: Twój kod poniżej



print("Liczba linków:", html.count('href="'))

domeny = []

linki = html.split('href="')

for link in linki[1:]:
    adres = link.split('"')[0]

    if "://" in adres:
        domena = adres.split("/")[2]

        if domena not in domeny:
            domeny.append(domena)

for domena in domeny:
    print(domena)