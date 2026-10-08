# ---------------------------------------------
#  Spojování podmínek: and a or
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Někdy nestačí jedna podmínka. Chceme třeba, aby platily dvě zároveň,
# nebo aby stačila aspoň jedna. K tomu jsou and a or.
#
#   and  ... a zároveň  – platí, jen když platí OBĚ podmínky
#   or   ... nebo       – platí, když platí ASPOŇ JEDNA podmínka


# and – musí platit obojí:
vek = 25
print(vek >= 18 and vek < 65)   # True – je zároveň dospělý i mladší 65


# or – stačí jedno:
den = "sobota"
print(den == "sobota" or den == "neděle")   # True – je to víkend


# Praktická ukázka. Obdélník má dvě strany a obě musí být kladné.
# Dřív bychom to řešili vnořeným if, teď stačí jeden řádek s or:
a = 5
b = -2

if a <= 0 or b <= 0:
    print("Strany musí být kladné.")
else:
    print("Obvod je", 2 * (a + b))


# ---
# Pozor: and/or spojují CELÉ podmínky, ne holá čísla.
# Všimni si, že nahoře máme porovnání dvakrát – zvlášť pro a a zvlášť pro b:
#
#     if a <= 0 or b <= 0:      # správně
#
# Když se to pokusíš zkrátit takhle, je to chyba:
#
#     if a or b <= 0:           # ŠPATNĚ
#
# Python to čte jako „(a)  nebo  (b <= 0)" – u prvního čísla žádné
# porovnání není. Vždycky napiš celé porovnání na OBOU stranách or / and.


# A vzpomínáš na „největší ze tří" z bonusového cvičení? S and se z toho stane
# jediná podmínka místo vnořených if:
x = 12
y = 25
z = 8

if x >= y and x >= z:
    print("Největší je", x)
elif y >= x and y >= z:
    print("Největší je", y)
else:
    print("Největší je", z)
