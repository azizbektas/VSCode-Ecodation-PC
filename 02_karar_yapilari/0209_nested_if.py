# nested if
# region ornek_1
"""
havaYagisliMi = False
havaSogukMu = False
i = 1
print("a")
if havaYagisliMi == True:
    if havaSogukMu == True:
        print("b")
    else:
        print("c")
else:
    if i == 0:
        print("d")
    else:
        print("e")
print("f")
"""
# endregion

# region ornek_2
"""
+   kullanıcı değer girecek
+   int dönüşümü yapılacak
+   kullanıcı 0 yada negatif değer girmemeli
+   0-100 arası yada 100+ olup/olmadığını bulan prog.
+   ekrana kullanıcı dostu çıktı verecek
"""
a = int(input("lütfen sayı giriniz \t : "))
if a > 0:
    if a < 100:
        print(f"{a} sayı 100 den küçüktür, pozitif")
    else:
        print(f"{a} sayı 100 den büyüktür, pozitif")
else:
    print("lütfen 0 yada negatif değer girmeyin")

# endregion
