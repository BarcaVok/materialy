# ---------------------------------------------
#  range a sum: posloupnost čísel
# ---------------------------------------------
# Někdy potřebujeme celou řadu čísel po sobě – třeba 0, 1, 2, 3, 4.
# Vypisovat je ručně by bylo zdlouhavé. Od toho je funkce range.
# Spusť soubor a sleduj výsledky.


# range(5) vyrobí čísla od 0 do 4 (pět čísel, ale poslední se NEpočítá).
# Když range vypíšeme přímo, ukáže se jen "návod", ne samotná čísla:
print(range(5))       # range(0, 5)   čísla zatím schovaná uvnitř


# Že jsou uvnitř opravdu čísla, si ověříme pomocí dalších funkcí.
# sum sečte všechna čísla v posloupnosti.
print(sum(range(5)))      # 10   protože 0 + 1 + 2 + 3 + 4 = 10


# len spočítá, kolik čísel v posloupnosti je.
print(len(range(5)))      # 5


# min a max najdou nejmenší a největší číslo v posloupnosti.
print(min(range(5)))      # 0
print(max(range(5)))      # 4   poslední je o jedna míň než 5


# range může začínat jinde než od nuly – dáme dvě čísla: OD, DO.
# Číslo DO se opět nepočítá.
print(sum(range(1, 5)))   # 10   sečte 1 + 2 + 3 + 4


# Pěkná ukázka síly range – součet čísel od 1 do 100 na jeden řádek:
print(sum(range(1, 101))) # 5050
