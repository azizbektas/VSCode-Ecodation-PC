# region ornek_1
"""
1→  sonsuz döngü içinde kullanıcın girdiği sayıların
    tek olanlarının ortalamasını bulalım
2→  çift sayı girmeye çalıştığında ekrana uyarı verelim
3→  programı continue kulllanmalıyız

tekSayilarToplami = 0
while True:
    a = int(input("lütfen sayı giriniz, çıkmak için -1 giriniz: "))
    if a == -1:
        break
    if a % 2 != 1:
        print("lütfen tek sayı giriniz")
        continue
    tekSayilarToplami += a
print(f"listedeki tek sayıların toplamı {tekSayilarToplami}")
"""
# endregion

# region ornek_2
"""
Kullanıcı aşağıdaki gibi bir seçim yaparak alt programları çalıştıracağız.
Hiç biri değil ise hatalı seçim diyeceğiz.
[1]     km→mil
[2]     mil→km
[3]     çık
"""
while True:
    secim = int(input("""
        [1]     km→mil
        [2]     mil→km
        [3]     çık
    """))
    if secim == 1:
        km = float(input("lütfen km bilgisi giriniz \t: "))
        mil = km * 0.62137
        print(f"girilen {km} değerinin mil hesaplaması {round(mil,2)}")
    elif secim == 2:
        mil= float(input("lütfen mil bilgisi giriniz \t: "))
        km  = mil / 0.62137
        print(f"girilen {mil} değerinin km hesaplaması {round(km,2)}")
    elif secim == 3:
        break
    else:
        print("hatalı seçim")

# endregion
