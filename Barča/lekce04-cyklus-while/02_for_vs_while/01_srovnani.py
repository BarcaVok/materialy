# ---------------------------------------------
#  for vs while – kdy použít který
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Oba cykly opakují. Liší se tím, kdy se hodí:
#   for    – když počet opakování známe předem (projít range nebo text)
#   while  – když počet neznáme a opakujeme, dokud platí nějaká podmínka


# Stejný úkol – vypsat čísla 1 až 5 – jde napsat obojím:

# Forem: počet opakování známe (pět čísel), for si počítání hlídá sám.
for cislo in range(1, 6):
    print(cislo)

# Whilem: totéž, ale počítadlo si musíme hlídat sami.
cislo = 1
while cislo <= 5:
    print(cislo)
    cislo = cislo + 1


# Když počet opakování známe, for bývá kratší a přehlednější.
# Některé úlohy ale forem nenapíšeš a bez while se neobejdeš – třeba:
#   opakuj, dokud uživatel nezadá správné heslo
#   opakuj, dokud hráč nechce skončit
