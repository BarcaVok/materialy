# Tahák – Lekce 1: První program

Rychlý přehled toho, co jsme se naučili. Klidně si ho vytiskni na A4.

## Výpis na obrazovku – `print`

```python
print("Ahoj")              # vypíše text
print("Věk:", 30)          # víc hodnot, oddělí je mezerou
print("Součet:", 3 + 8)    # počítat můžeš i uvnitř printu
```

## Datové typy

- `str` – text (řetězec), třeba `"Anna"`
- `int` – celé číslo, třeba `30`
- `float` – desetinné číslo, třeba `3.14` (s tečkou, ne čárkou)

## Počítání s čísly

```python
+  -  *  /       # sčítání, odčítání, násobení, dělení
-5               # negace (mínus)
17 // 5   -> 3   # celočíselné dělení (zahodí zbytek)
17 % 5    -> 2   # zbytek po dělení (modulo)
2 ** 3    -> 8   # mocnina (dvě na třetí)
```

Pořadí jako v matematice: nejdřív `*` a `/`, potom `+` a `-`.
Závorky mají přednost: `(2 + 3) * 4`.

## Počítání s textem

```python
"Py" + "Ladies"   -> "PyLadies"    # spojení textu
"ha" * 3          -> "hahaha"      # opakování textu
```

## Proměnné

```python
jmeno = "Anna"     # ulož hodnotu do proměnné
print(jmeno)       # použij ji pod jejím jménem
jmeno = "Petra"    # hodnotu můžeš kdykoli přepsat
```

Jména proměnných: malými písmeny, začínají písmenem, bez mezer
(víc slov spoj podtržítkem) a výstižně: `mesto`, `cena`, `oblibena_barva`.

## Vstup od uživatele – `input`

```python
jmeno = input("Jak se jmenuješ? ")      # input VŽDY vrátí text
vek = int(input("Kolik ti je let? "))   # převod textu na celé číslo
strana = float(input("Strana: "))       # převod na desetinné číslo
```

## Častá chyba

`input` vrací text, i když napíšeš číslo. Než s ním počítáš, převeď ho:

```python
vek = input("Věk: ")
print(vek + 1)            # CHYBA – text a číslo nejde sčítat

vek = int(input("Věk: "))
print(vek + 1)            # správně
```
