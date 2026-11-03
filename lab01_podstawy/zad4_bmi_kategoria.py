# Lab 01 – Zadanie 4 (☆, dodatkowe): Kategoria BMI
#
# Rozbuduj kalkulator BMI: po obliczeniu wypisz także kategorię (wg WHO):
#     BMI < 18.5          -> niedowaga
#     18.5 <= BMI < 25    -> waga prawidłowa
#     25 <= BMI < 30      -> nadwaga
#     BMI >= 30           -> otyłość
#
# To zadanie wymaga instrukcji if / elif / else, którą dokładnie poznasz
# w labie 03. Spróbuj już teraz – składnię znajdziesz na slajdach.

# TODO: Twój kod poniżej

 HEAD
masa = float(input("Podaj mase w kg "))
wzrost = float(input("Podaj wzrost w metrach "))

bmi = masa/wzrost**2

print(f"twoje BMI wynosi {bmi:.2f}")

if bmi < 18.5:
    print("niedowaga")
elif bmi < 25:
    print("waga prawidlowa")
elif bmi < 30:
    print("nadwaga")
else:
    print("otylosc")

masa = float(input("Podaj mase: "))
wzrost = float(input("Podaj wzrost w metrach: "))
bmi = masa / (wzrost)**2
bmi_2 = round(bmi,2)

print(f"{bmi_2:.2f} ")

if (bmi_2<18.5):
    print("Niedowaga")
elif (bmi_2<25):
    print("Waga prawidlowa")
elif (bmi_2<30):
    print("Nadwaga")
else:
    print("Otylosc")
 2a807b6 (Lab-4_1)
