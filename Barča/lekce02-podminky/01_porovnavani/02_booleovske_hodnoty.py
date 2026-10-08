# ---------------------------------------------
#  Booleovské hodnoty (True / False)
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Výsledek porovnání je vždycky jedna ze dvou hodnot: True, nebo False.
# Říká se jim booleovské hodnoty (podle matematika George Boolea).
# Je to nový datový typ – stejně jako číslo nebo text.


# Píšou se přesně takhle, s velkým prvním písmenem a bez uvozovek:
print(True)
print(False)


# Výsledek porovnání si můžeš uložit do proměnné a používat dál:
je_plnolety = 20 >= 18
print(je_plnolety)     # True


teplota = 5
je_zima = teplota < 0
print(je_zima)         # False – 5 stupňů, ještě nemrzne


# Pozor na rozdíl:
#   =   ukládá hodnotu do proměnné   (vek = 20)
#   ==  porovnává, jestli se rovnají  (vek == 20)
vek = 20            # do proměnné vek uložíme 20
print(vek == 20)    # True   ptáme se, jestli je v ní 20
print(vek == 18)    # False
