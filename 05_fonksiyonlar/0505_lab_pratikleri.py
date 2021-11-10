# region ornek_1
"""
1→ kullanıcıya fonk. içinde "sadece sayısal değer girin"
2→ kullanıcıya fonk. içinde "sadece pozitif değer girin"

def hataKodu100():
    print("sadece sayısal değer giriniz")

def hataKodu200():
    print("sadece pozitif değer giriniz")

yas = input("lütfen yaşınızı giriniz :")
if yas.lstrip("-").isdigit():
    yas = int(yas)
    if yas<0:
        hataKodu200()
    else:
        print(f"yaşınız {yas}")
else:
    hataKodu100()
"""
# endregion

# region ornek_2
"""
1→ fonksiyona değer gönderelim, dairenin çapını hesaplayalım
2→ int kontrolü yapalım
def hataKodu100():
    print("sadece sayısal değer giriniz")


def hataKodu200():
    print("sadece pozitif değer giriniz")


def alan(yaricap):
    alan = 22/7*yaricap**2
    print(f"yarıçağı {yaricap} olan dairin alanı {alan}")


yCap = input("lütfen yarıçap giriniz :")
if yCap.lstrip("-").isdigit():
    yCap = int(yCap)
    if yCap < 0:
        hataKodu200()
    else:
        alan(yCap)
else:
    hataKodu100()
"""
# endregion

# region ornek_3
"""
1→ günün saatine göre Günaydın/Merhaba diyen program yazalım
2→ ad bilgisi argüman olarak fonksiyona gönderilsin

def selamlasma(ad):
    import datetime
    saat = datetime.datetime.now().hour
    if saat<12:
        print(f"günaydın {ad}")
    else:
        print(f"merhaba {ad}")


selamlasma(input("karşıdan gelen arkadaşın ismi : "))
"""
# endregion
