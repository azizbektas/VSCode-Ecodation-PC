# region break_continue_neden_kullanilir
"""
break     → döngüyü sonlandırır
continue  → tepeye geri döndürecek
"""
# endregion

# region break
"""
i = 1
print("a")
while i<11:
    if i==15:
        print("b")
        break
    print(f"{i}. döngü")
    i += 1
print("c")
"""


# endregion

# region continue
"""
i = 1
print("a")
while i < 11:
    if i == 5:
        i += 1
        continue
    print(f"{i}. döngüdeyim")
    i += 1
print("b")
"""
# endregion

# region break_continue_mix
"""
i = 1
print("a")
while i < 100:
    if i % 7 == 0:
        i += 1
        continue
    elif i % 15 == 0:
        break
    print(f"{i}. döngüdeyim")
    i += 1
print("b")
"""
# endregion

# region ornek
"""
Kullanıcı istediği kadar sayı girsin. Çıkmak için -1 tuşlasın.
Döngü sonunda girilen en büyük sayıyı ekrana yazdıralım.
Adım sayısı belli olmadığı için sonsuz döngü içinde çözümleyeceğiz

eb, say = 0, 0
while True:
    sayi = int(input("lütfen sayı giriniz, çıkmak için -1 \t: "))
    if sayi == -1:
        break
    say += 1
    if sayi > eb:
        eb = sayi
if say:
    print(f"girdiğiniz listedeki en büyük sayı {eb}")
else:
    print("hiç bir sayı girmediniz")
"""
# endregion
