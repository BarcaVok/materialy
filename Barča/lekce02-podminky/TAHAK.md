# Tahák – Lekce 2: Podmínky a rozhodování

Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.

## Porovnávání

Výsledek je vždy `True`, nebo `False`.

```python
5 == 5    -> True    # je rovno? (POZOR: dvě rovnítka)
5 != 3    -> True    # není rovno?
5 > 3     -> True    # větší
5 < 3     -> False   # menší
5 >= 5    -> True    # větší nebo rovno
3 <= 2    -> False   # menší nebo rovno
"Anna" == "anna"  -> False   # velké a malé písmeno není totéž
```

## Booleovské hodnoty

`True` / `False` – nový datový typ. Výsledek porovnání si lze uložit:

```python
je_plnolety = vek >= 18
```

Pozor na rozdíl:

```python
=    # ukládá hodnotu do proměnné   (vek = 20)
==   # porovnává, jestli se rovnají  (vek == 20)
```

## if / elif / else

```python
if znamka == 1:
    print("Výborně!")       # když platí první podmínka
elif znamka == 2:
    print("Chvalitebně.")   # jinak když platí tato
else:
    print("Něco jiného.")   # jinak (nepovinné)
```

## and / or / not

```python
vek >= 18 and vek < 65   # A ZÁROVEŇ – platí, jen když platí obě
den == "so" or den == "ne"   # NEBO – stačí aspoň jedna
not prsi                 # NE – otočí True <-> False
(je_vikend and hezky) or je_svatek   # závorky seskupí a spojí víc podmínek
```
