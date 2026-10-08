# Tahák – Lekce 3: Funkce a cyklus for

Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.

## Užitečné vestavěné funkce

```python
len("Ahoj")        -> 4     # délka textu
abs(-7)            -> 7     # absolutní hodnota
round(3.14159)     -> 3     # zaokrouhlení na celé číslo
round(3.14159, 2)  -> 3.14  # na daný počet desetinných míst
min(3, 8, 2)       -> 2     # nejmenší z hodnot
max(3, 8, 2)       -> 8     # největší z hodnot
sum(range(1, 6))   -> 15    # součet čísel v posloupnosti
```

## `range` – posloupnost čísel

```python
range(5)         -> 0, 1, 2, 3, 4    # od nuly, druhé číslo se NEpočítá
range(1, 6)      -> 1, 2, 3, 4, 5    # od-do
range(0, 10, 2)  -> 0, 2, 4, 6, 8    # od, do, krok
```

## Cyklus for

```python
for cislo in range(3):
    print(cislo)     # odsazené = opakuje se
```

`cislo` mění hodnotu každé kolo. Jméno si volíš ty.

## Sbírání výsledku

```python
soucet = 0
for cislo in range(1, 6):
    soucet = soucet + cislo
```

## Procházení textu

```python
for pismeno in "Ahoj":
    print(pismeno)
```

## Vnořené cykly

```python
for radek in range(3):
    for hvezda in range(5):
        ...          # vnitřní cyklus proběhne celý pro každé kolo vnějšího
```
