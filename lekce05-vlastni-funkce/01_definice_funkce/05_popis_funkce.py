# ---------------------------------------------
#  Popis funkce
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Funkci, kterou napíšeš dneska, budeš za měsíc číst znovu. A funkci od
# někoho jiného čteš bez toho, že bys viděla, jak ji psal. Proto se hned
# na první řádek těla píše popis, čemu se říká docstring:

def zkontroluj_heslo(heslo, min_delka=8):
    """Vypíše, jestli je heslo dost dlouhé.

    heslo      text, který se kontroluje
    min_delka  nejmenší povolená délka, celé číslo větší než nula
    """
    if len(heslo) < min_delka:
        print(heslo, "– moc krátké")
    else:
        print(heslo, "– dost dlouhé")


zkontroluj_heslo("kolo")
zkontroluj_heslo("pyladies2026")


# Tři uvozovky na začátku a na konci dovolí text na víc řádků. Mezi ně
# patří jedna věta o tom, co funkce dělá, a pak co čeká od každého
# parametru – včetně toho, jaké hodnoty mají smysl.


# Python popis nijak nehlídá. Když do min_delka pošleš nulu, funkce se
# nezlobí a projde cokoli:
zkontroluj_heslo("kolo", 0)


# Popis je vzkaz pro člověka. Python ho ale umí najít a ukázat:
help(zkontroluj_heslo)


# Ve VS Code se ten stejný text objeví sám, když na jméno funkce najedeš
# myší nebo když za ni napíšeš levou závorku.
