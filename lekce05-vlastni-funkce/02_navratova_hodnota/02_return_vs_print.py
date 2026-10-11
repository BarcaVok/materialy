# ---------------------------------------------
#  return vs. print
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Tyhle dvě funkce vypadají na první pohled skoro stejně:

def vypis_dph(cena):
    print(cena * 1.21)


def spocitej_dph(cena):
    return cena * 1.21


# Když je zavoláš, obě ukážou to samé číslo:
vypis_dph(100)
print(spocitej_dph(100))


# Rozdíl je vidět, až když si výsledek zkusíš uložit:
vysledek_vypisu = vypis_dph(100)
vysledek_vypoctu = spocitej_dph(100)
print("z vypis_dph:", vysledek_vypisu)
print("ze spocitej_dph:", vysledek_vypoctu)


# Proměnná vysledek_vypisu je None. Funkce vypis_dph číslo vypsala,
# ale ven nic nepředala – a když funkce nemá return, vrací Python
# právě None (tedy „nic"). S None se dál počítat nedá:
#
# print(vysledek_vypisu + 50)     # TypeError


# Proto se funkce většinou píšou tak, že spočítají a vrátí, a vypisování
# nechají na tom, kdo je volá. Funkce, která výsledek vypíše, umí jednu
# jedinou věc a navždycky. Funkce, která ho vrátí, ho podá dál a volající
# si vybere, co s ním:
print("Cena s DPH:", spocitej_dph(100), "Kč")
print("Dohromady:", spocitej_dph(100) + spocitej_dph(250), "Kč")


# Vybrat si může i to, že výsledek pošle do další funkce. Děláš to celou
# dobu – print(spocitej_dph(100)) je přesně ono. Tady ho pošleme funkci
# round, kterou znáš z vestavěných funkcí:
print(round(spocitej_dph(99.9), 2))


# Nebo se podle výsledku rozhodne:
if spocitej_dph(1000) > 1000:
    print("Tohle už je na dražší objednávku.")


# Vypsat výsledek hned se zdá jednodušší. print ale píše do terminálu
# a terminál je jen jedno z míst, kde výsledek může skončit – jinde to
# bude webová stránka, okno aplikace nebo soubor. Funkce, která spočítá
# a vrátí, poslouží všude.
