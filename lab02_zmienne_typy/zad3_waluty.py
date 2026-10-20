# Lab 02 – Zadanie 3 (★): Przelicznik walut
#
# Program wczytuje kwotę w złotych i wypisuje jej równowartość w EUR i USD,
# zaokrągloną do 2 miejsc po przecinku, np. dla 425 zł:
#     425.00 PLN = 100.00 EUR
#     425.00 PLN = 111.84 USD
#
# Kursy są STAŁE (na potrzeby zadania – nie są to aktualne kursy NBP):

#EUR_RATE = 4.25   # 1 EUR = 4.25 PLN
#USD_RATE = 3.80   # 1 USD = 3.80 PLN

# TODO: Twój kod poniżej
kwota_w_zl = float(input("Podaj kwotę w złotych "))

EUR_RATE = 4.25   
USD_RATE = 3.80 

kwota_w_eur = kwota_w_zl / EUR_RATE
kwota_w_usd = kwota_w_zl / USD_RATE

print(f"{kwota_w_zl:.2f} PLN = {kwota_w_eur:.2f} EUR")
print(f"{kwota_w_zl:.2f} PLN = {kwota_w_usd:.2f} USD")
