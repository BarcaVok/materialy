# ---------------------------------------------
#  Když se proměnná mění výpočtem
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# V prvním souboru se proměnná z podmínky měnila tím, že jsme se znovu
# zeptali uživatele. Můžeme si ji taky spočítat. Cyklus pak běží,
# dokud výpočet nedojde tam, kam chceme.


# Máme provaz dlouhý 100 cm. Přestřihneme ho napůl, jednu polovinu zase
# napůl, a tak dál. Kolikrát musíme střihnout, než bude kus kratší než 1 cm?
delka = 100
strihnuti = 0
while delka > 1:
    delka = delka / 2       # měníme proměnnou z podmínky
    strihnuti = strihnuti + 1
    print("Střihnutí", strihnuti, "– délka:", delka, "cm")
print("Počet střihnutí:", strihnuti)


# Proměnné strihnuti se říká počítadlo. Hodí se vždycky, když
# potřebuješ vědět, kolikrát cyklus proběhl.
