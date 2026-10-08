# Tahák – Lekce 4: Cyklus while

Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.

## Cyklus while

Opakuje tělo, **dokud platí podmínka**. Počet opakování nemusíme znát předem.

```python
heslo = input("Heslo: ")
while heslo != "pyladies":       # podmínka – platí True/False
    print("Špatně.")             # odsazené řádky = tělo cyklu
    heslo = input("Heslo: ")     # měň proměnnou z podmínky, jinak nekonečno
print("Vítej!")                  # neodsazené = až po skončení cyklu
```

Podmínce se říká **ukončovací podmínka**. Python ji kontroluje před každým
průchodem: platí → tělo se provede, neplatí → cyklus skončí.

## break – druhý východ z cyklu

```python
while True:              # podmínka platí vždycky
    odpoved = input("Pokračovat? (ano/ne) ")
    if odpoved == "ne":
        break            # break = okamžitě opusť cyklus
```

Z cyklu se tedy dostaneš dvěma způsoby: podmínka přestane platit, nebo `break`.
`while True` se bez `break` neobejde – je to jediná cesta ven.

## continue – přeskoč zbytek průchodu

```python
while True:
    jmeno = input("Jméno: ")
    if jmeno == "konec":
        break
    if jmeno == "":
        continue     # zpátky nahoru, zbytek těla se přeskočí
    print(jmeno)
```

`break` cyklus opustí, `continue` ukončí jenom jeden průchod.

## Počítadlo

Chceš vědět, kolikrát cyklus proběhl? Přidej si proměnnou:

```python
heslo = input("Heslo: ")
pokusy = 0
while heslo != "pyladies":
    heslo = input("Heslo: ")
    pokusy = pokusy + 1
```

Stejně se dá sčítat (`soucet = soucet + cislo`) nebo počítat písmena.

## Nekonečný cyklus

Když se ukončovací podmínka nikdy neporuší, program „zamrzne".
Zastavíš ho dole ve VS Code v panelu **Terminál**: klikni do něj a zmáčkni
**Ctrl+C**, nebo program zabij ikonou **koše** vpravo v panelu.

**Častá chyba:** v těle cyklu nezměníš proměnnou z podmínky → běží pořád.

```python
cislo = 1
while cislo <= 5:
    print(cislo)         # chybí cislo = cislo + 1
```

## Náhodné číslo

```python
from random import randrange   # patří na první řádek souboru

randrange(1, 7)    # náhodné číslo od 1 do 6 (druhé číslo se NEpočítá)
randrange(1, 21)   # náhodné číslo od 1 do 20
```

## for vs while

```text
for    -> znám počet opakování (projít range nebo text)
while  -> neznám počet, opakuju dokud platí podmínka
```
