# ---------------------------------------------
#  Nekonečný cyklus
# ---------------------------------------------
# Spusť soubor a odpovídej, dokud tě to bude bavit.
#
# Když se ukončovací podmínka nikdy neporuší, cyklus běží donekonečna –
# tomu se říká nekonečný cyklus. Program pak „zamrzne" a musíš ho zastavit
# sama: klikni dole do panelu Terminál a zmáčkni Ctrl+C. Druhá možnost je
# ikona koše vpravo v tom panelu – ta program rovnou zabije.


# Takhle nekonečný cyklus vznikne omylem – NESPOUŠTĚJ to, běželo by
# to pořád. Zapomněli jsme cislo zvětšovat, takže je pořád 1
# a podmínka cislo <= 5 pořád platí:
#
# cislo = 1
# while cislo <= 5:
#     print(cislo)
#
# Nejčastější chyba u while je přesně tahle: v těle cyklu chybí řádek,
# který mění proměnnou z podmínky.


# Někdy ale nekonečný cyklus chceme schválně – třeba menu, které se
# opakuje, dokud uživatelka neřekne dost. Napíšeme while True (podmínka
# platí vždycky) a ven se dostaneme příkazem break, který už známe.
while True:
    odpoved = input("Chceš pokračovat? (ano/ne) ")
    if odpoved == "ne":
        break
    print("Pokračujeme!")
print("Konec.")


# Na odpověď se tady ptáme jen na jednom místě. Podmínka while True se
# nekontroluje proti žádné proměnné, takže input nemusíme psát i před
# cyklem, jako jsme to dělali v souboru 01.


# while True se bez breaku neobejde – je to jediná cesta ven.
# break funguje stejně i uvnitř cyklu for.
