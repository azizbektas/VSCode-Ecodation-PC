# region ornek_1
"""
Sonsuz döngü içinde: favori aylar girilecek
daha önce ekledi isek uyaracak

favoriAylar = []
while True:
    fav = input("favori ayınız, çıkmak için -1: ")
    if fav=="-1":
        break
    if fav in favoriAylar:
        print("daha önce ekledi")
        continue
    favoriAylar.append(fav)
print(favoriAylar)
"""
# endregion

# region ornek_2
"""
Kesişen Liste Örneği

liste1 = [1, 2, 3, 4, 5]
liste2 = [4, 5, 6, 7 ,8]
ortakElemanlar = []
for i in liste1:
    if i in liste2:
        ortakElemanlar.append(i)
print(ortakElemanlar)
"""

# endregion

# region ornek_3
"""
Birleşim Liste Örneği

stokDepo1 = [1, 2, 3, 4, 5]
stokDepo2 = [4, 5, 6, 7 ,8]
tekilListe = stokDepo1.copy()
for item in stokDepo2:
    if item not in tekilListe:
        tekilListe.append(item)
print(tekilListe)
"""
# endregion