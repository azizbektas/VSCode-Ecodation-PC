# region ornek_1
"""
carp uygulaması da yapalım
carp(4, 2)
carp(4, 2, 3)
carp(4, 2, 3, 5)



def carp(a, b, c=1, d=1):
    print(a*b*c*d)


carp(4, 2)
carp(4, 2, 3)
carp(4, 2, 3, 5)
"""
# endregion

# region ornek_2
"""
def carp(a, b, c, ayrac="x"):
    print(f"{a} {ayrac} {b} {ayrac} {c} = {a*b*c}")


carp(2,3,4)
"""
# endregion

# region ornek_3
"""
1→ parametre olarak girilen değerin mutlak değerini alsın
2→ kullanıcıya sadece sayısal değer girilmeli
3→ parametre gönderilmediğinde hata vermesin -1 değerinin mutlak değerini yaz


def mutlakDeger(a=-1):
    if str(a).lstrip("-").isdigit():
        a = int(a)
        if a<0:
            a *= -1
        print(f"mutlak değer → {a}")        
    else:
        print("lütfen sayısal değer giriniz")

mutlakDeger("on")
"""
# endregion

# region ornek_4
"""
1→ kayıtOl fonksiyonu yazılacak
2→ T.C. Kimlik, Ad, Email isimli üç adet argüman
3→ mail girilmez ise hata vermeyecek çıktıda '@' yazılacak
4→ ad girilmez ise hata vermeyecek çıktıda 'isimsiz' yazılacak
"""

def kayıtOl(tc, ad="isimsiz", email="@"):
    print("kayıt başarılı")
    print(f"{tc} {ad} {email}")


kayıtOl("1111111")

# endregion
