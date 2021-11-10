# region fonksiyon_turu_3_parametre_almayan_deger_donduren
"""
Fonksiyon tanımlama anında argüman almaz, değer döndürür
a = round(123.555)
print(a)
print(round(123.555))
"""
# endregion

# region ornek_1
"""
print("break point")
def topla():
    s1 = int(input("S1 : "))
    s2 = int(input("S2 : "))
    return s1 + s2

sonuc = topla()
print(sonuc)
"""
# endregion

# region peki_ne_zaman_return_kullaniriz
"""
"""
# endregion

# region ornek_2
"""
def topla():
    s1 = int(input("s1 : "))
    s2 = int(input("s2 : "))
    return s1+s2
    print("burası print edilmeyecek")


sonuc = topla()
print(sonuc)
"""
# endregion