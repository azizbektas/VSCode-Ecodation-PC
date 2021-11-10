# region ornek_1
"""
Listeye 
sonsuz döngü içinde öğrenci ekleyeceğiz

ogrenciListesi= []
while True:
    ogrenci = input("listeye eklenecek öğrenci, çıkmak için -1 : ")
    if ogrenci == "-1":
        break
    ogrenciListesi.append(ogrenci)
for i in ogrenciListesi:
    print(i)
"""
# endregion


# region ornek_2
"""
Benzer örneği bu kez
Ekle-Sil-Listele menüsü ile genişletelim

ogrenciListesi = []
print("""
        #[1]     Ekle
        #[2]     Sil
        #[3]     Listele
        #[4]     Çık
""")
while True:
    secim = int(input("lütfen seçiminizi giriniz... : "))
    if secim == 1:
        ogrenci = input("listeye eklenecek öğrenci,")
        ogrenciListesi.append(ogrenci)
    elif secim == 2:
        ogrenci = input("listeden silinecek öğrenci,")
        ogrenciListesi.remove(ogrenci)
    elif secim == 3:
        for i in ogrenciListesi:
            print(i)
    elif secim == 4:
        break
    else:
        print("hatalı seçim")
   
"""
# endregion


# region ornek_3
"""
Ad-Soyad-Not1-Not2 
Sonsuz döngü içinde girilecek, not ortalamaları baz alınarak
en düşük, en yüksek not listelenecek

notOrtalamalari = []
while True:
    ogrenciAdSoyad = input("lütfen ad soyad giriniz, çıkmak için -1 : ")
    if ogrenciAdSoyad=="-1":
        break
    n1 = int(input("lütfen n1 notu giriniz: "))
    n2 = int(input("lütfen n2 notu giriniz: "))
    if not 0<=n1<=100 or not 0<=n2<=100:
        print("lütfen [0-100] arası değer giririniz")
        continue
    notOrtalamalari.append((n1+n2)/2)
for i in notOrtalamalari:
    print(i)
minimum,maksimum = 9999999999, 0
for i in notOrtalamalari:
    if i<minimum:
        minimum=i
    if i>maksimum:
        maksimum=i
print(f"en düşük not → {minimum} - en yüksek not {maksimum}")
"""
# endregion


# region ornek_4
"""
Benzer örneği bu kez
Çan eğrisi mantığı ile ortalamanın altında kalan notları listeleyelim



notOrtalamalari = []
while True:
    ogrenciAdSoyad = input("lütfen ad soyad giriniz, çıkmak için -1 : ")
    if ogrenciAdSoyad=="-1":
        break
    n1 = int(input("lütfen n1 notu giriniz: "))
    n2 = int(input("lütfen n2 notu giriniz: "))
    if not 0<=n1<=100 or not 0<=n2<=100:
        print("lütfen [0-100] arası değer giririniz")
        continue
    notOrtalamalari.append((n1+n2)/2)
genelOrtalama = sum(notOrtalamalari)/len(notOrtalamalari)
for i in notOrtalamalari:
    print(i)
minimum,maksimum = 9999999999, 0
for i in notOrtalamalari:
    if i<minimum:
        minimum=i
    if i>maksimum:
        maksimum=i
print(f"en düşük not → {minimum} - en yüksek not {maksimum}")

for i in notOrtalamalari:
    if i<genelOrtalama:
        print(f"dönem tekrar yapacak öğrencinin notu {i}")
"""
# endregion


# region ornek_5
"""
İki basamaklı sayıyı → metne dönüştüren uygulama yapalım
Örn; 95
doksan beş

birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
sayi = 95
print(f"{onlar[sayi//10]} {birler[sayi%10]}")
"""
# endregion
