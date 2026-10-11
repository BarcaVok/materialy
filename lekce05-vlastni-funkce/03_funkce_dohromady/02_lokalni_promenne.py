# ---------------------------------------------
#  Proměnné uvnitř funkce
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.
#
# Proměnná, která vznikne uvnitř funkce, patří jenom té funkci.
# Venku o ní Python neví.

def cena_s_dph(cena):
    print("Uvnitř funkce je cena:", cena)
    dan = cena * 0.21
    return cena + dan


# Parametr je na tom stejně. Tady je proměnná cena i venku,
# a přesto si funkce žije se svou vlastní:
cena = 500

print("Výsledek:", cena_s_dph(100))
print("Venku je cena:", cena)


# Kdyby to tak nebylo, každá funkce by nám přepisovala proměnné
# v celém programu a nikdo by se v tom nevyznal.


# Druhým směrem to ale funguje. Funkce vidí proměnné, které vznikly venku:
jmeno = "Jana"


def predstav_se():
    print("Ahoj, já jsem", jmeno)


predstav_se()


# Vypadá to pohodlně. Takovou funkci ale nejde přenést jinam, protože mimo
# tenhle program žádné jmeno není. A z prvního řádku její definice není
# poznat, s čím vlastně pracuje. Když si to, co potřebuje, vezme jako
# parametr, je to vidět hned:
def predstav_se(jmeno):
    print("Ahoj, já jsem", jmeno)


predstav_se("Jana")
predstav_se("Petra")


# A teď ta chyba. Proměnná dan vznikla uvnitř funkce cena_s_dph,
# takže tenhle řádek skončí hláškou NameError: name 'dan' is not defined
print(dan)
