
#region ornek_1
"""
n1, n2 = int(input("lütfen 1. snv notunu giriniz \t : ")), int(input("lütfen 2. snv notunu giriniz \t : "))
ort = (n1+n2)/2
if ort>=85:
    print(f"yıl sonu notunuz {ort}, başarı durumu PEKİYİ")
elif ort>=70:
    print(f"yıl sonu notunuz {ort}, başarı durumu İYİ")
elif ort>=55:
    print(f"yıl sonu notunuz {ort}, başarı durumu ORTA")
elif ort>=45:
    print(f"yıl sonu notunuz {ort}, başarı durumu GEÇER")
else:
    print(f"yıl sonu notunuz {ort}, başarı durumu GEÇEMEZ")
"""
#endregion

#region ornek_2
"""
s1 = int(input("l. s1. giriniz : "))
s2 = int(input("l. s2. giriniz : "))
s3 = int(input("l. s3. giriniz : "))
if s1<s2:
    s1, s2 = s2, s1
if s1<s3:
    s1, s3 = s3, s1
if s2<s3:
    s2, s3 = s3, s2
print(f"{s1}>{s2}>{s3}")
"""
#endregion

#region ornek_3
"""
a = int(input("lütfen a kenarını giriniz \t : "))
b = int(input("lütfen b kenarını giriniz \t : "))
if a==b:
    print(f"karenin alanı {a*b}")
else:
    print(f"dikdörtgenin alanı {a*b}")
"""
#endregion

#region ornek_4
"""
kisaKenar = int(input("lütfen kısa kenarını giriniz \t : "))
uzunKenar = int(input("lütfen uzun kenarını giriniz \t : "))
if kisaKenar>uzunKenar:
    print("kısa kenar uzun girilemez")
else:
    print(f"dörtgenin çevresi {2*(kisaKenar + uzunKenar)}")
"""
#endregion

#region ornek_5
"""
a = int(input("lütfen 1. s giriniz \t : "))
b = int(input("lütfen 2. s giriniz \t : "))
if a%b==0:
    print(f"{a} sayısı {b} sayısına tam bölünür")
else:
    print(f"{a} sayısı {b} sayısına tam bölünemez")
"""
#endregion


# ödev →
"""
    - Kullanıcıdan bir sayı alınır.
        - Pozitifse karesini yazdırın.
        - Negatifse karekökünü yazdırın.
        - 0'sa sıfır yazsın
"""



# ödev →
"""
    - Klavyeden iki tane fiyat verisi alınır.
    - Eğer bu fiyat verileri düzgünse;
        - Eğer ödenecek tutar 200TL den fazlaysa, ikinci ürüne
            %25 indirim yapılacaktır.
        - Değilse bişey yapılmayacak.
    - 150,300 -> Ürünlerin fiyatı .. TL ve .. TL'dir. İkinci ürüne
     .. TL indirim yapılmıştır. Borcunuz : ..TL'dir.
"""

# ödev →
"""
    - ax2+bx+c = 0
    - Kullanıcıdan a,b,c değerleri alınır. Bu degerler uygunsa ;
        - delta = b2 - 4ac
        - delta>0. iki kök : (-b+kök(delta))/2a,(-b-kök(delta))/2a
        - delta=0. iki kök : k1=k2=-b/2a
        - delta<0. kök yoktur.
"""

# ödev →
"""
    - Kullanıcıdan vize ve final notları istenir.
    - Eğer vize ve final notları int ise;
        - Eğer ikisi de 0-100 arasındaysa;
            - ortalama = vizenin %40+ finalin %60
            - ortalama: 
                90-100 -> AA
                75-90  -> BB
                60-75  -> CC
                50-60  -> DD
                0-50   -> FF.
                Ekrana harf karşılığını yazınız.
        - 0-100 arasında değilse lütfen 0-100 arasında giriniz yazacak
"""


# ödev →
"""
    - Yakıt tüketimini hesaplayan uygulama yazalım
        - Yakıt tipi kullanıcıdan alınacak benzin/dizel
        - Aracınızın 100 km.'deki ortalama yakıt tütekimi kullanıcıdan alınacak
        - Anlık yakıt kuru internetten bakılabilir
"""