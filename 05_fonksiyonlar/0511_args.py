# region args_giris
"""
fonksiyondaki argüman sayısı ile çağırırken kullandığım argüman sayısı
aynı olmalı

def topla(a, b, c):
    print(f"{a} + {b} + {c} = {a+b+c}")

topla(a=2, b=3)
"""
# endregion

# region gecici_cozum
"""
Not→ ancak yazarken dikkat! önce positional argument yazılmalı

def topla(c=5, a, b):
    print(f"{a} + {b} + {c} = {a+b+c}")

topla(b=2, a=3)
"""
# endregion

# region degisken_sayida_parametre_gonderimi
"""
1→ argüman olarak , ile değişken sayıda değer gönderirim
2→ fonksiyon, gelen değerleri liste elemanı olarak işler
3→ for döngüsü içinde istediğim algoritmayı yürütürüm

def topla(*args):
    print(type(args))
    topla = 0
    for i in args:
        topla += i
    print(topla)

topla(2,3,5)
topla(2,3,5,5)
""" 

# endregion

# region ornek_1
"""
# önce manuel olarak liste elemanlarını toplamayı pratik edelim
...
...

# sum yöntemi liste elemanlarını kolayca toplayacaktır
def topla(*args):
    print(f"liste elemanları toplamı → {sum(args)}")

topla(2, 3, 5)
topla(2, 3)
topla(2, 3, 6, 8, 10)
"""
# endregion

# region ornek_2
"""
def ortalama(*args):   
    print(f"liste elemanlarının ortalaması → {sum(args)/len(args)} ")


ortalama (6, 8, 10, 12, 20)
"""
# endregion

# region ornek_3
"""
Argüman olarak gönderdiğim list'i tekil olarak ekrana yazsın. 
tekilListe(3, 5, 7, 10, 12, 5, 7)
output → 3, 5, 7, 10, 12

def tekilListe(*args):
    yeniListe = []
    for i in args:
        if i not in yeniListe:
            yeniListe.append(i)
    print(yeniListe)



tekilListe(3, 5, 5, 10, 12, 3, 13)
"""
# endregion



"""
def favDerslerim(*args):
    for i in args:
        print(i)

favDerslerim("matematik","biyoloji", "fizik", "kimya")
"""


"""
def hobilerim(*args, ad):
    print(f"{ad} öğretmeniminin hobileri")
    for i in args:
        print(i, end= " ")


hobilerim("basketbol", "koşu", "gezi", "müzik", ad = "Aziz")
"""