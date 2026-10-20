# Lab 03 – Zadanie 5 (☆, dodatkowe): Jaki to trójkąt?
#
# Program wczytuje trzy długości boków (float) i wypisuje:
#   - "Nie da się zbudować trójkąta", jeśli nie spełniają nierówności trójkąta
#     (każdy bok musi być krótszy od sumy dwóch pozostałych),
#   - w przeciwnym razie rodzaj: "równoboczny", "równoramienny" albo "różnoboczny",
#   - dodatkowo "prostokątny", jeśli a² + b² = c² dla najdłuższego boku c
#     (porównuj z tolerancją: abs(x - y) < 1e-9).

# TODO: Twój kod poniżej
l1 = float(input("Podaj dlugość boku pierwszego "))
l2 = float(input("Podaj dlugość boku drugiego "))
l3 = float(input("Podaj dlugość boku trzeciego "))

if l1 > l2 and l1 > l3:
    c = l1
    a = l2
    b = l3

elif l2 > l1 and l2 > l3:
    c = l2
    a = l1
    b = l3
else:
    c = l3
    a = l1
    b = l2

if l2 + l3 > l1 and l1 + l2 > l3 and l1 + l3 > l2:
    if l1 == l2 == l3:
        print("równoboczny")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("równoramienny")
    else:
        print("różnoboczny")
    if abs((a**2 + b**2) - c**2) < 1e-9:
        print("prostokątny")
else:
     print("Nie da się zbudować trójkąta")
    
