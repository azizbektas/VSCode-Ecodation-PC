# region inline_for_giris
# tek satırda for yazmak mümkün inline for
"""
liste =[]
for i in range(1, 9):
    liste.append(i)
print(liste)


liste = [i for i in range(1, 9)]
print(liste)

row = ["piyon" for i in range(8)]
print(row)
"""
# endregion

# region ornek
"""
Haftanın 1. Günü Pazartesi  Haftanın 2. Günü Salı ...
"""
hafaninGunleri = ["", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

liste = [f"Haftanın {i}. Günü {hafaninGunleri[i]}" for i in range(1, 8) if i<=3]
print(liste)
# endregion