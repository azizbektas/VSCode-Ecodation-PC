# region ornek_1
"""
kullanıcı sayı girecek
int dönüşümü yapılacak
girilen sayının tam bölenleri ekrana yazılacak

s = int(input("l. s. giriniz \t: "))
for i in range(1, s+1):
    if s % i == 0:
        print(i, end = " ")
"""
# endregion


# region ornek_2
"""
girilen sayıya kadar olan asal sayıları 
ekrana yazdıran programı yazalımkullanıcı sayı girecek
say = 0
son = int(input("l. son değeri. giriniz \t: "))
for i in range(2, son+1):
    for j in range(1, i):
        if i % j == 0:
            say +=1
    if say<2:
        print(i, end= " ")
    say = 0
"""
# endregion

# region ornek_3
"""
obeb = 0
s1 = int(input("lütfen 1. s . gi "))
s2 = int(input("lütfen 2. s . gi "))
for i in range(1, min(s1, s2)+1):
    if s1 % i == 0:
        if s2 % i == 0:
            obeb = i
print(obeb)
"""
# endregion

# region ornek_4
"""
kullanıcının girdiği sayı TAU sayısı mıdır?
TAU sayısı : 
24 → 1, 2, 3, 4, 6, 8, 12, 24 → 24 % 8 == 0 TAU dur.
15 → 1, 3, 5, 15 → 15 % 4 != 0 TAU değildir.
Anlamı: pozitif bölenleri sayısına bakıldığında mod 0 ise TAU dur.

sayac = 0
sayi = int(input("lütfen sy giriniz: "))
for i in range(1, sayi + 1):
    if sayi % i == 0:
        sayac += 1
if sayi % sayac == 0:
    print("TAUDUR")
else:
    print("TAU DEĞİLDİR")
"""
# endregion

# region ornek_5
"""
mükemmel sayı kendisi haricindeki tüm çarpanlarının
toplamı kendisini veren sayıdır
6   → 1, 2, 3 → toplamı 6 mükemmel sayı
24 → 1, 2, 3, 4, 6, 8, 12 → toplamı 36 mükemmel sayı değildir
toplam = 0
sayi = int(input("lütfen sy giriniz: "))
for i in range(1, int(sayi/2)+1):
    if sayi%i == 0:
        toplam += i
if toplam == sayi:
    print("mükemmeldir")
else:
    print("mükemmel değildir")
"""
# endregion



# ödev →
"""
    - Kullanıcının girdiği 2sayı arasındaki değerleri,
    her zaman küçükten büyüğe sıralayan for döngüsü yazın.

    1,10 -> 1,2,3,4,5,6,7,8,9
    10-1 -> 1,2,3,4,5,6,7,8,9
"""
