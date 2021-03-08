# region ornek_1
"""
delta örneği

"""
# endregion


# region ornek_2
"""
ortalama

"""
# endregion


# region ornek_3
"""
saat bilgisini saniyeye dönüştürsün
"""
saat = 2
saniye = 3600
print("Saat: ", saat)
print("Ekrandaki saat biriminin saniye karşılığı →", saat*saniye, " sn.")
# endregion

# formatter shift + alt + f
sayi = 562
kalan = sayi % 10
birler = kalan // 1
kalan = sayi % 100
onlar = kalan // 10
kalan = sayi % 1000
yuzler = kalan //100
toplamDegeri = birler + onlar + yuzler
print(yuzler, onlar, birler)
print(toplamDegeri)