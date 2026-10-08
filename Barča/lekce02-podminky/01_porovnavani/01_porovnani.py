# ---------------------------------------------
#  Porovnávání hodnot
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Python umí porovnávat hodnoty – zeptat se třeba „je pět větší než tři?".
# Na každou takovou otázku odpoví True (pravda), nebo False (nepravda).


# Je rovno?  Píše se DVĚMA rovnítky ==
# (jedno rovnítko = už známe, to ukládá hodnotu do proměnné)
print(5 == 5)     # True   pět se rovná pěti
print(5 == 3)     # False  pět se nerovná třem


# Není rovno?  Píše se !=
print(5 != 3)     # True   pět není tři
print(5 != 5)     # False  pět se rovná pěti, podmínka „není rovno" tedy neplatí


# Větší >  a  menší <
print(5 > 3)      # True   pět je opravdu větší než tři
print(5 < 3)      # False  pět není menší než tři


# Větší nebo rovno >=  a  menší nebo rovno <=
print(5 >= 5)     # True   pět je rovno pěti (stačí, aby platila jedna z možností)
print(3 <= 2)     # False  tři není menší ani rovno dvěma


# Porovnávat se dá i text – Python kouká, jestli jsou řetězce stejné:
print("Anna" == "Anna")   # True   oba řetězce jsou úplně stejné
print("Anna" == "anna")   # False  liší se první písmeno, velké a malé není totéž
