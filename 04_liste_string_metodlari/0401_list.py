# region list_giris
"""
katilimciListesi = ["alperen","kübra","batu","umut"]
meyveler = ["karpuz", "üzüm"]
plakalar = [34, 35]
print(katilimciListesi)
print(meyveler)
print(plakalar)
"""
# endregion

# region bos_liste
"""
isimler = []
print(isimler)
print(type(isimler))
plakalar = []
print(isimler)
"""
# endregion

# region ornek_listeler
# duplicate??? evet
"""
sayilar = [11, 15, 7, 12, 1, 0, 3.14, 15]
print(sayilar)
ogrenciListesi = ["ali", "mustafa", "ali"]
print(ogrenciListesi)
"""
# endregion

# region index
"""
sayilar = [11, 15, 7, 12, 1, 0, 3.14, 12, 13]
print(sayilar[1])
print(sayilar[0])
print(sayilar[7]) # çok doğru yaklaşım değil
print(sayilar[-1])
print(sayilar[-2])
"""
# endregion

# region guncelleme_degistirme
"""
sayilar = [11, 15, 7, 12]
print(sayilar)
sayilar[1] = 34
print(sayilar)
"""

"""
sayilar = [11, 15, 7, 12]
print(sayilar)
sayilar[1] = sayilar[3]
print(sayilar)
"""
# endregion

# region listenin_uzunlugu_eleman_sayisi
"""
sayilar = [11, 15, 7, 12, 15, 25, 30]
print(len(sayilar))
print(sayilar[len(sayilar)-1])
print(sayilar[len(sayilar)//2])
"""
# endregion

# region del_talimati_instruction
"""
sayilar = [11, 15, 7, 12, 15]
print(sayilar)
del sayilar[1]
print(sayilar)
[11, 15, 7, 12, 15]
[11, 0, 7, 12, 15]
del sayilar #intellisense
print(sayilar)
"""
# endregion

# region for_loop_ile_oku
"""
sayilar = [12, 36, 9, 5, 3, 74]
print("30 dan büyük olan sayıların listesi")
for i in sayilar:
    if i>30:
        print(i)
"""
# endregion

# region for_loop_ile_liste_elemanlarını_topla
"""
toplam = 0
sayilar = [11, 15, 7, 12, 1, 0, 3.14, 15]
for i in sayilar:
    toplam += i
print(f"listedeki elamanları toplamı → {toplam}")
"""
# endregion

# region for_loop_ile_listedeki_tek_sayi_adedi
"""
adet = 0
sayilar = [11, 15, 7, 12, 1, 15]
for i in sayilar:
    if i%2!=0:
        adet += 1
print(f"listedeki tek sayı adedi → {adet}")
"""
# endregion