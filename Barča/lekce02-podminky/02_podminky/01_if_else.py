# ---------------------------------------------
#  Rozhodování: if / else
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Umíme porovnávat – dostaneme True, nebo False. Teď podle toho
# necháme program rozhodnout, co udělá.
#
# Zápis:
#   if podmínka:
#       kód, který se spustí, když podmínka platí (je True)
#
# Za if napíšeme podmínku, pak DVOJTEČKU. Řádky pod ní odsadíme
# (posuneme doprava – ve VS Code stačí klávesa Tab). 
# Odsazení říká Pythonu „tohle patří do if-u".


vek = 20

if vek >= 18:
    print("Jsi plnoletá.")
    print("Můžeš volit.")

# Oba odsazené řádky se spustí, protože vek >= 18 je True.
# Zkus změnit vek třeba na 15 a spusť znovu – nevypíše se nic.


# Často chceme udělat něco i pro opačný případ. K tomu je else
# („jinak"). Spustí se, když podmínka NEPLATÍ (je False):
teplota = 5

if teplota > 15:
    print("Je hezky, jde se ven.")
else:
    print("Radši si vezmi bundu.")

# Vždycky se spustí právě jedna z těch dvou větví, nikdy obě.


# ---
# Odsazení je důležité – rozhoduje o tom, co do if-u patří,
# a začátečnice na něm chybují nejčastěji.
#
# Řádek BEZ odsazení už do if-u nepatří a spustí se pokaždé,
# ať podmínka platí, nebo ne:
if teplota > 15:
    print("Tohle jen když je teplo.")
print("Tohle se vypíše vždycky.")

# A naopak řádky, které do if-u patří, musí být odsazené STEJNĚ –
# nejlíp pořád klávesou Tab. Když to nesedí, Python soubor ani
# nespustí a vypíše chybu IndentationError. Například tady je
# třetí řádek odsazený víc:
#
#     if vek >= 18:
#         print("Jsi plnoletá.")
#             print("Můžeš volit.")     # IndentationError!
#
# Až tuhle chybu uvidíš (a uvidíš ji často), zkontroluj, jestli máš
# všechny řádky v bloku odsazené na stejné úrovni.
