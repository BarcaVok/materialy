# ---------------------------------------------
#  Na ukázku: kreslení s želvou (turtle)
# ---------------------------------------------
# TODO: najít cloudové/online prostředí, kde turtle spolehlivě poběží.
#       Lokálně turtle často zlobí kvůli instalaci a nastavení, proto si
#       tenhle soubor jen SPOLEČNĚ ukážeme (promítneme) – není určený
#       k samostatnému spouštění doma.
# TODO: celou tuhle ukázku ještě přepracovat tak, aby na ní bylo pořádně
#       vidět chování cyklu for (jak se krok po kroku opakuje) – např.
#       pomalejší kreslení / zvýraznění každého průchodu cyklem.
#
# Turtle je „želva", která po obrazovce kreslí čáru. Umí dvě věci:
# popojet dopředu a otočit se. Právě tady je krásně vidět síla cyklu for –
# místo abychom stejný příkaz psali pořád dokola, necháme ho zopakovat.

import turtle


# Čtverec: čtyřikrát „popojeď dopředu a otoč se o 90 stupňů".
for strana in range(4):
    turtle.forward(100)     # popojeď o 100 kroků
    turtle.left(90)         # otoč se o 90 stupňů doleva


# Zkus si pohrát s čísly:
#   3 strany a otočka 120 stupňů  → trojúhelník
#   5 stran a otočka  72 stupňů   → pětiúhelník
#   8 stran a otočka  45 stupňů   → osmiúhelník
# (Otočka je vždycky 360 děleno počtem stran.)


turtle.done()               # nechá okno otevřené, dokud ho nezavřeš
