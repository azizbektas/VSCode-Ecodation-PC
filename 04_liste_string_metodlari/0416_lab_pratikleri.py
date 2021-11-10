# region ornek
"""
Tam bölünüp/bölünmediğini bulalım
Int kontrolü yapalım
"""
s1 = input("Lütfen Sayı Giriniz: ")
s2 = input("Lütfen Sayı Giriniz: ")
if s1.isdigit() and s2.isdigit():
    s1, s2 = int(s1), int(s2)
    if s1%s2==0:
        print("tam bölünür")
    else:
        print("tam bölünemez")
else:
    print("lütfen sayısal değer giriniz")
# endregion


