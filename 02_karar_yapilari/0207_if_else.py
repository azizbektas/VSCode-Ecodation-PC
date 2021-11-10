# if-else : evet döndüğünde bir şey yap, hayır döndüğünde başka bir şey yap
#region ornek_1
"""
havaDurumu = "yağmurlu"
print("a")
if havaDurumu == "yağmurlu":
    #print("şemsiye al lütfen")
    print("b")
else:
    #print("şemsiye almana gerek yok")
    print("c")
print("d")
"""

#endregion

#region ornek_2
"""
engeleDegdiMi = True
can, skor = 3, 0
if engeleDegdiMi:
    can -=1
    print(f"{can} canınız kaldı")
else:
    skor += 1
    print(f"{skor} anlık skorunuz")
"""
#endregion

#region ornek_3
"""
sayi = int(input("l. s .g : "))
if sayi % 2 != 0:
    print(f"{sayi} sayı tektir")
else:
    print(f"{sayi} sayı çifttir")
"""
#endregion