# mantıksal operatörler → logical operatörler
# koşul ifadelerini birleştirmek için kullanılır
"""
1→ ve       and
2→ veya     or
3→ değil    not
"""


# region and
"""
print(5 == 5 and 15 > 5)
print(5 == 5 and 15 < 5)
print(5 == 15 and 15 > 5)
print(5 == 15 and 15 < 15)
"""
# endregion


# region or
"""
print(5 == 5 or 15 > 5)
print(5 == 5 or 15 < 5)
print(5 == 15 or 15 > 5)
print(5 == 15 or 15 < 15)
"""
# endregion


# region not
"""
print(not 5 == 5)
print(5 != 5)
"""
# endregion


# region ornek_1
"""
iç içe if ile yaptığımız pratiğimizi tekrar edelim
0<sayı<100 arasında pozitiftir

a = int(input("a değeri giriniz: "))

# if a>0 and a<100:
#    print(f"{a} sayısı 100 den küçük pozitif")

#if 0 < a < 100:
    #print(f"{a} sayısı 100 den küçük pozitif")
  """  
# endregion


# region ornek_2
"""
code.org sitesine giriş yapacak olan kullanıcı
4,5,6 yaşları için kurs 1'e hoş geldin
dışında yaşı olanlar ise kurs 1'e uygun değilsin mesajı verelim

yas = int(input("lütfen yaş giriniz: "))
if yas>6 or yas<4:
    print("kurs 1 e uygun değilsin")
else:
    print("kurs 1 e hoş geldiniz")
"""    
# endregion


# region ornek_3
"""
toplam = 0
while True:
    sayi = int(input("lütfen sayı giriniz. Çıkmak için 0 tuşuna basınız. \t"))
    if sayi == 0:
        break
    if sayi<0 or sayi %2 == 1:
        print("Negatif ve tek sayı giremezsin")
        continue
    toplam += sayi
print(toplam)
"""
# endregion
