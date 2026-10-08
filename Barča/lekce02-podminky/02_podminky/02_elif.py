# ---------------------------------------------
#  Víc možností: elif
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# if a else zvládnou dvě možnosti. Když jich je víc, přidáme mezi ně
# elif (zkratka za „else if" – tedy „jinak když"). Můžeš jich mít
# kolik chceš.
#
# Zápis:
#   if podmínka1:
#       ...
#   elif podmínka2:
#       ...
#   else:
#       ...


znamka = 2

if znamka == 1:
    print("Výborně!")
elif znamka == 2:
    print("Chvalitebně.")
elif znamka == 3:
    print("Dobře.")
else:
    print("Příště to půjde líp.")


# Python zkouší podmínky odshora dolů a zastaví se u PRVNÍ, která platí.
# Její větev spustí a zbytek přeskočí. Proto se vždycky spustí
# nejvýš jedna větev.


# else je nepovinné. Když ho vynecháš a žádná podmínka neplatí,
# neudělá se prostě nic:
teplota = 25

if teplota < 0:
    print("Mrzne.")
elif teplota < 15:
    print("Chladno.")
elif teplota < 25:
    print("Příjemně.")

# Při teplotě 25 neplatí ani jedna podmínka (25 není menší než 25),
# takže se nevypíše nic. Zkus změnit teplotu na 10.
