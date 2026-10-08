# ---------------------------------------------
#  Jak cyklus skončí: ukončovací podmínka a break
# ---------------------------------------------
# Spusť soubor víckrát – pokaždé to dopadne jinak.
#
# V prvním souboru jsme psali:
#
#   while heslo != "pyladies":
#
# Té podmínce se říká ukončovací podmínka. Python ji zkontroluje vždycky
# před každým průchodem cyklem:
#   platí   → tělo cyklu se provede a kontrola se opakuje
#   neplatí → cyklus skončí a program pokračuje pod ním


# Tímhle řádkem si přidáme funkci randrange, kterou má Python připravenou.
# randrange(1, 7) vybere náhodné číslo od 1 do 6 – jako hod kostkou.
from random import randrange


# Házíme kostkou tak dlouho, dokud nepadne šestka.
hod = randrange(1, 7)
while hod != 6:
    print("Padlo", hod, "- házíme znovu.")
    hod = randrange(1, 7)     # DŮLEŽITÉ: měníme proměnnou z podmínky
print("Šestka! Můžeš začít.")


# Když padne šestka hned napoprvé, tělo cyklu neproběhne ani jednou.
# Podmínka se totiž kontroluje už před prvním průchodem.


# Všimni si posledního řádku v cyklu: kdybychom kostkou znovu nehodili,
# hod by zůstal pořád stejný a cyklus by nikdy neskončil.
#
# (Tři různé běhy tohohle programu ukazuje obrázek cyklus_while_behy.png.)


# ---------------------------------------------
#  Druhý způsob, jak z cyklu ven: break
# ---------------------------------------------
# Někdy chceme cyklus opustit dřív, než podmínka přestane platit.
# Od toho je příkaz break – okamžitě z cyklu vyskočí.

# Zase házíme na šestku, ale po jedničce to vzdáme.
hod = randrange(1, 7)
while hod != 6:
    if hod == 1:
        print("Padla jednička, končíme.")
        break                 # break = okamžitě opusť cyklus
    print("Padlo", hod, "- házíme znovu.")
    hod = randrange(1, 7)
print("Konec hry.")


# Tenhle cyklus má tedy dva východy:
#   1) padne šestka  → podmínka hod != 6 přestane platit
#   2) padne jednička → break nás z cyklu vyhodí rovnou
