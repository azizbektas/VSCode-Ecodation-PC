# region ornek_1
"""
ogrenci1 = ["Alp", "Besi", 90,	90]
ogrenci2 = ["Batu", "Koçhan", 10, 90]
ogrenci3 = ["Emir", "Besi", 100,	90]
ogrenci4 = ["Umut", "Ahmet", 95, 80]
ogrenci5 = ["Aziz", "Bektaş", 15, 10]
ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5]

for i in ogrenciler:
    if (i[2]+i[3])/2<50:
        print(f"{i[0]} {i[1]} → KALDI")
    else:
        print(f"{i[0]} {i[1]} → GEÇTİ")
"""
# endregion

# region ornek_2
""""""
ogrenci1 = [
    "Alp",
    "Besi",
    90,
    90,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.",
    1997
]
ogrenci2 = [
    "Batu",
    "Koçhan",
    10,
    90,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.",
    1998
]
ogrenci3 = [
    "Emir",
    "Besi",
    100,
    90,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.",
    2008
]
ogrenci4 = [
    "Umut",
    "Ahmet",
    95,
    80,
    "Video, size görüşünüzü kanıtlamak için güçlü bir yol sunar. Çevrimiçi Video'ya tıkladığınızda, eklemek istediğiniz videoya ait ekleme kodunu yapıştırabilirsiniz. Belgenize en iyi uyan videoyu çevrimiçi olarak aramak için bir anahtar sözcük de yazabilirsiniz.",
    2000
]
ogrenci5 = [
    "Aziz",
    "Bektaş",
    15,
    10,
    "Kısa CV",
    1980
]
ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5]
i = 1
for item in ogrenciler:
    if len(item[4]) > 30:
        cv = f"{item[4][:30]}..."
    else:
        cv = item[4]
    if (item[2]+item[3])/2 < 50:
        print(f"{i} {(2021-(item[-1]))} {item[0]} {item[1]} {cv}→ KALDI")
    else:
        print(f"{i} {(2021-(item[-1]))} {item[0]} {item[1]} {cv} → GEÇTİ")
    i += 1

# endregion
