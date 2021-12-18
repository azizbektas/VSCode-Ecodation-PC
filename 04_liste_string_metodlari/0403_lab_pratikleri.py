# region ornek_1
"""
sayı dizisi tanımlanacak
for loop içinde arama yaparak
aradığınız ... indisli eleman bulundu
mesajı verilecek

sayilar = [11, 5, 36, 78, 99, 2]
n = 0
for i in sayilar:
    if i == 99:
        break
    n += 1
print(f"aradığınız {n} indisli eleman bulundu")
"""
# endregion

# region ornek_2
"""
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
Aradığınız Öğrenci: mehmet
mehmet isimli öğrenci bulundu
Aradığınız Öğrenci: murat
murat isimli öğrenci bulunamadı

ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
while True:
    ogrenciAdi = input("Aradığınız Öğrenci Giriniz, Çıkmak İçin ç : ")
    if ogrenciAdi == "ç":
        break
    for i in ogrenciListesi:
        if i == ogrenciAdi:
            print(f"{ogrenciAdi} isimli öğrenci bulundu")
            break
    else:
        print(f"{ogrenciAdi} isimli öğrenci bulunamadı")
"""
# endregion

# region ornek_3

"""
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
Aradığınız Öğrenci: mehmet
mehmet listenin 3. sırasındaki öğrencidir
Aradığınız Öğrenci: murat
sınıfta murat isimli öğrenci yoktur
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa", "önder"]
print(len(ogrenciListesi))
listem = range(len(ogrenciListesi))
print(listem)

while True:
    ogrenciAdi = input("Aradığınız Öğrenci Giriniz, Çıkmak İçin ç : ")
    if ogrenciAdi == "ç":
        break
    for i in range(len(ogrenciListesi)):
        if ogrenciListesi[i] == ogrenciAdi:
            print(f"{ogrenciAdi} listenin {i+1}. sırasındaki öğrencidir")
            break
    else:
        print(f"sınıfta {ogrenciAdi} isimli öğrenci yoktur")
"""
# endregion

# region ornek_4
"""
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa", "önder"]
for i in range(len(ogrenciListesi)):
    print(ogrenciListesi[i])
"""    
# endregion



# ödev →
"""
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
Aradığınız Öğrenci: mehmet
mehmet listenin 3. sırasındaki öğrencidir

Aradığınız Öğrenci: murat
sınıfta murat isimli öğrenci yoktur
"""


# ödev →
"""
rakamlar = [6, 2, 7, 3, 5]
Çıktı:
["ALTI", "İKİ", "YEDİ", "ÜÇ, "BEŞ"]
"""


# ödev →
"""
rakamlar = ["elma", "armut", "erik", "şeftali"]
Çıktı:
ismi e ile başlayan meyve elma
ismi e ile başlayan meyve erik
"""



