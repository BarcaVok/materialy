# ---------------------------------------------
#  if uvnitř if (vnořené podmínky)
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# if můžeš dát dovnitř jiného if. Hodí se, když chceš něco ověřit
# TEPRVE potom, co platí něco jiného. Vnitřní blok jen odsadíš
# ještě o kus dál.


venku_prsi = True
mam_destnik = False

if venku_prsi:
    print("Venku prší.")
    # Tenhle if řešíme jen tehdy, když prší:
    if mam_destnik:
        print("Naštěstí mám deštník.")
    else:
        print("A nemám deštník – zmoknu.")
else:
    print("Je sucho, pohoda.")

# Všimni si dvou úrovní odsazení: vnější if řeší déšť,
# vnitřní if (odsazený víc) řeší deštník.


# ---
# Kdy vnořený if a kdy elif?
#
# elif se hodí, když se rozhoduješ mezi možnostmi JEDNÉ otázky
# (jaká je známka? jaká je teplota?) – platí právě jedna větev.
#
# Vnořený if se hodí, když se ptáš na DVĚ různé věci za sebou
# a druhá má smysl jen podle výsledku první (prší? a když prší,
# mám deštník?).
