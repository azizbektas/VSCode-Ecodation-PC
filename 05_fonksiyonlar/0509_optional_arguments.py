# region optional_arguments_default_value
"""
Namı diğer → değişken sayıda parametre gönderimi
Fonksiyonu tanımlama anında argümanlarına default değer atayabiliriz
Bu sayede, değişken sayıda argüman gönderebiliriz


a= zorunlu
b = zorunlu
c = opsiyonel
def topla(a, b, c=5):
    print(f"{a} + {b} + {c} = {a+b+c}")


topla(a=2, b=3)
"""
# endregion


# region ornek_1
"""
default argüman ve non-default argüman birlikte kullanılır mı EVET
ancak önce non-default argümanlar yazılmalı

def topla(a=2, b, c):
    print(f"{a} + {b} + {c} = {a+b+c}")


topla(b=3, c= 10)
"""
# endregion


# region ornek_2
"""
opsiyonel olmasına rağmen fonk. çağırırken değer ataması yapar isek
fonksiyonda tanımlı değeri ezer!!!!

def topla(a, b, c=5):
    print(f"{a} + {b} + {c} = {a+b+c}")


topla(a= 2, b=3, c= 10)
"""
# endregion