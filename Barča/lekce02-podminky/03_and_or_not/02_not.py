# ---------------------------------------------
#  Otočení podmínky: not
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# not znamená „ne". Otočí hodnotu naruby: z True udělá False
# a naopak. Hodí se, když chceš reagovat na to, že něco NEPLATÍ.


print(not True)     # False
print(not False)    # True


# not před podmínkou ji obrátí:
prsi = False
print(not prsi)    # True – „neprší"


# Typické použití – reagovat na opak:
prihlaseny = False

if not prihlaseny:
    print("Nejprve se přihlas.")


# ---
# not umí otočit i celou složenou podmínku. Dej ji do závorky
# a před ni napiš not – tím obrátíš výsledek CELÉ závorky.
heslo_ok = True
jmeno_ok = False

# „platí obojí" je True jen tehdy, když sedí heslo i jméno:
print(heslo_ok and jmeno_ok)        # False

# not (…) otočí výsledek té závorky – „neplatí obojí":
print(not (heslo_ok and jmeno_ok))  # True

if not (heslo_ok and jmeno_ok):
    print("Přihlášení selhalo.")

# Čti to jako „není pravda, že platí heslo i jméno zároveň".
# Závorka je důležitá – řekne Pythonu, co přesně má not otočit.
