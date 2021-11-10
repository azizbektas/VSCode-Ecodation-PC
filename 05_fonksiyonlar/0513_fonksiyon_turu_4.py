# region fonksiyon_turu_4_parametre_alan_deger_donduren
"""
Fonksiyon tanımlama anında argüman alır, değer döndürür
"""
# endregion

# region ornek_1
"""
def mutlakDeger(a):
    if a<0:
        a *= -1
    return f"mutlak değer → {a}"
#print(mutlakDeger(5))
mDegeri = mutlakDeger(-20)
print(mDegeri)
"""


# endregion

# region ornek_2
"""
fonksiyona sıcaklık değeri olarak göndereceğim 'derece' argümanını 
'fahrenheit' olarak geriye döndüren prog.

def cToF(s):
    # s → sıcaklık, derece
    return s*9/5+32


print(cToF(35))
"""
# endregion

# region ornek_3
"""
D. Tarihi [Gün] : 30
D. Tarihi [Ay] : 2
Şubat Ayı 30 Çekmez

gunler = ["", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
aylar = ["",
         "ocak", "şubat", "mart",
         "nisan", "mayıs", "haziran",
         "temmuz", "ağustos", "eylül",
         "ekim", "kasım", "aralık"
         ]

def ayKontrol(a, g):
    if gunler[a]<g:
        print(f"{aylar[a]} ayı {g} çekmez")
        return False
    else:
        return True

while True:
    dTarihiGun = int(input("D. Tarihi [Gün]"))
    dTarihiAy= int(input("D. Tarihi [Ay]"))
    if not ayKontrol(dTarihiAy,dTarihiGun ):
        continue
    dTarihiYil= int(input("D. Tarihi [Yıl]"))
    break
print(f"{dTarihiGun} {aylar[dTarihiAy]} {dYil}")
"""
# endregion