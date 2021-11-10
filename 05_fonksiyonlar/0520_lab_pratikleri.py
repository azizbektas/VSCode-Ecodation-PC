# region ornek_1
"""
5^5 + 4^4 + 3^3 + 2^2 + 1^1

def topla(n):
    if n<=1:
        return 1
    else:
        return pow(n, n) + topla(n-1)
    
print(topla(5))
"""
# endregion

# region ornek_2
"""
Birazdan parola üretme algoritması yazacağız
harf listesi için aşağıdaki script'i deneyebilirsiniz
"""

harfler = "A B C Ç D E F G Ğ H I İ J K L M N O Ö P R S Ş T U Ü V Y Z"
listeHalinde = harfler.split()
print(listeHalinde) 

# endregion 

# region ornek_3
"""
parolaUret()
10 karakterli olacak → for loop 10
random üretilen 1-3 listeden eleman seçecek
1- 0-9
2- a-z
3- A-Z

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# "a","b","c","ç","d","e","f","g","ğ","h","i","ı","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"
# "A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"



rakamlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
kHarfler = ["a","b","c","ç","d","e","f","g","ğ","h","i","ı","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
bHarfler = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
import random
parola = ""
def parolaUret():
    global parola
    sec = random.randint(1,3)
    if sec==1:
        parola += str(random.choice(rakamlar))
    elif sec==2:
        parola += random.choice(kHarfler)
    else:
        parola += random.choice(bHarfler)

while True:
    for i in range(10):
        parolaUret()
    print(parola)
    parola = ""
    print()

"""
# endregion 

# region ornek_4
"""
def kartBilgiVer(k):
    return f"{k['ad']} {k['soyad']} {k['bankaAdi']} {k['para']}"

def atmBilgiVer(a):
    return f"{a['ad']} {a['para']}"

def ayniMi(k, a):
    if k['bankaAdi'] == a['ad']:
        return True
    else: 
        return False

def paraYatir(k, a, miktar):
    k['para'] += miktar
    a['para'] += miktar
    if not ayniMi(k, a):
        k['para'] -= miktar*0.03
        a['para'] += miktar*0.03
    print(f"{miktar} para yatırıldı. ATM'de {a['para']} TL. oldu")

def paraCek(k, a, miktar):
    if a['para']>=miktar:
        if k['para']>=miktar:
            k['para'] -= miktar
            a['para'] -= miktar
            if not ayniMi(k, a):
                k['para'] -= miktar*0.03
                a['para'] += miktar*0.03
                print(f"kartınızdan {miktar*0.03} TL. ücret alındı")
            print(f"{miktar} TL. Çekildi. Atm'de {a['para']} kaldı. Hesabınızda da {k['para']} kaldı.")
        else:
            print(f"Bakiyenizde bu kadar para yok. En fazla {k['para']} TL. çekebilirsiniz")
    else:
        print(f"ATM'de Bu KAdar PAra Yok {a['para']} miktar çekebilirsiniz...")

kart = {
    "ad": "ali",
    "soyad" : "kemal",
    "bankaAdi": "zirat",
    "para": 100
}

atm = {
    "ad":"halk",
    "para":350
}


print(kartBilgiVer(kart))
print(atmBilgiVer(atm))
paraYatir(kart, atm, 100)
print("-"*50)
print(kartBilgiVer(kart))
print(atmBilgiVer(atm))
paraCek(kart, atm, 50)
print("-"*50)
print(kartBilgiVer(kart))
print(atmBilgiVer(atm))
"""
# endregion