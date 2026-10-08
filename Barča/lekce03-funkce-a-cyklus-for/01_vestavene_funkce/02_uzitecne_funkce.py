# ---------------------------------------------
#  Užitečné funkce: len, abs, round, min, max
# ---------------------------------------------
# Python má spoustu hotových funkcí. Projdeme si ty, které se hodí
# při počítání a práci s textem. Spusť soubor a sleduj výsledky.


# len (z anglického length = délka) vrátí délku textu – kolik má znaků.
slovo = "Ahoj"
print(len(slovo))     # 4   slovo "Ahoj" má čtyři písmena


# Argument můžeme dát rovnou, bez proměnné:
print(len("PyLadies"))    # 8


# A protože nám len výsledek vrací, můžeme s ním dál počítat:
delka = len("kolo")
print(delka + 1)      # 5


# abs (absolutní hodnota) – „zapomene" na znaménko mínus.
# Hodí se třeba na rozdíl dvou čísel, když nás nezajímá směr.
print(abs(-7))        # 7
print(abs(7))         # 7
print(abs(3 - 10))    # 7   z -7 udělá 7


# round zaokrouhlí desetinné číslo.
print(round(3.14159))     # 3   bez dalšího údaje zaokrouhlí na celé číslo
print(round(3.7))         # 4


# round umí zaokrouhlit i na určitý počet desetinných míst –
# napíšeme to jako druhý argument (oddělený čárkou).
print(round(3.14159, 2))  # 3.14   dvě desetinná místa


# min najde nejmenší a max největší z hodnot.
# Do závorek můžeme dát víc čísel oddělených čárkou.
print(min(3, 8, 2))       # 2   nejmenší
print(max(3, 8, 2))       # 8   největší


# Funkce se dají kombinovat s tím, co už umíme –
# třeba použít výsledek rovnou ve výpočtu nebo v porovnání:
print(max(10, 20) + 5)    # 25
print(min(4, 9) < 5)      # True   nejmenší je 4, a 4 je menší než 5
