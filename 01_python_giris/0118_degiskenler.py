#region ilk_giris
#variable - değişkenler
"""
skor = 12
print(skor)

name = "mehmet"
print(name)
"""
#endregion

#region notation
"""
#camel casing
okulNumarasi = 271
ad = "Emir"
soyad = "Besi"
sinavNotu = 99
print(okulNumarasi, ad, soyad, sinavNotu)
"""
"""
#undercore casing
okul_numarasi = 271
ad = "Emir"
soyad = "Besi"
sinav_notu = 99
print(okul_numarasi, ad, soyad, sinav_notu)
"""
#endregion

#region degisken_isimlendirme_kurallari
"""
Değişken İsimlendirme Kuralları
1- harf veya alt çizgi ile başlamalıdır
2- rakam ile başlayamaz
3- ilk harf dışındakiler, harf, sayı, alt çizgi olabilir
4- alt çizgi dışında alfa sayısal karakterlerimiz (%, #, $...) kullanılamaz
5- case sensitive
6- anahtar kelimeler if, pass, while, def bunlar kullanılamaz
7- türkçe karakter kullanmamaya özen gösterelim
"""


#1- harf veya alt çizgi ile başlamalıdır
"""
okul = "okan üniv."
birinci = "adana"
_birinci = "adana"
1nci= "adana"
"""


#2- rakam ile başlayamaz
"""
_34istanbul = "en güzel şehir"
"""

#3- ilk harf dışındakiler, harf, sayı, alt çizgi olabilir
"""
plaka34 = "istanbul"
print(plaka34)
"""
#4- alt çizgi dışında alfa sayısal karakterlerimiz (%, #, $...) kullanılamaz
"""
plaka&34 = "ist"
"""



#5- case sensitive
"""
ad = "ali"
print(Ad)
"""

#6- anahtar kelimeler if, pass, while, def, for bunlar kullanılamaz
"""
def = "definiton"

#keyword listesini görelim →
import keyword
print(keyword.kwlist)
"""


#7- türkçe karakter kullanmamaya özen gösterelim
"""
öğrenci = "Ali"
ogrenci = "ezgi"
print(ogrenci)
"""
#endregion