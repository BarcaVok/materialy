# ---------------------------------------------
#  Vnořené cykly (cyklus v cyklu)
# ---------------------------------------------
# Cyklus můžeme dát dovnitř jiného cyklu. Říká se tomu vnořený cyklus.
# Pravidlo: pro KAŽDÝ průchod vnějšího cyklu proběhne celý vnitřní cyklus.
# Spusť soubor a sleduj výsledky.


# Představ si hru o třech kolech a v každém kole dva pokusy.
# Vnějším cyklem jsou kola, vnitřním pokusy v rámci jednoho kola:
for kolo in range(1, 4):
    print("Kolo", kolo)
    for pokus in range(1, 3):
        print("  pokus", pokus)

# Odsazení určuje, co je uvnitř čeho: vnitřní cyklus je odsazený uvnitř
# vnějšího a řádek "Kolo" se provede jednou za kolo, "pokus" dvakrát.


# Vnořený cyklus se hodí, když chceme víc hodnot na JEDEN řádek a pak
# skočit na další. Vypíšeme třeba mini kalendář – tři týdny pod sebou,
# každý s čísly dnů 1 až 7. Vnitřní cyklus vypíše jeden řádek (týden),
# vnější ho zopakuje. Pomůže end (drží řádek) a prázdný print() (zalomí):
for tyden in range(1, 4):
    for den in range(1, 8):
        print(den, end=" ")       # dny 1 až 7 vedle sebe
    print()                       # po celém týdnu skoč na nový řádek
