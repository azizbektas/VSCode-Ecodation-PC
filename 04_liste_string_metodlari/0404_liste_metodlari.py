# region append→eleman_ekler_listenin_sonuna
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"{meyveler} listemizin ilk hali")
meyveler.append("karpuz")
print(f"{meyveler} listemizin son hali")
"""
# endregion

# region insert→eleman_ekler_istediginiz_indekse
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
#meyveler.insert(2, "portakal")
meyveler.insert(44, "portakal")
#meyveler.insert("portakal", 3) # bu atama mümkün değil önce index
print(f"listemizin son hali → {meyveler}")
"""
# endregion

# region remove→listeden_siler
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
# meyveler.remove("muz")
meyveler.remove("muzz")
print(f"listemizin son hali → {meyveler}")
"""
# endregion

# region pop→listeden_siler
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
#print(meyveler.pop()) son elemanı
print(meyveler.pop(2)) #o indeksli elemanı siler
print(f"listemizin son hali → {meyveler}")
sebzeler = []
sebzeler.pop()
"""
# endregion

# region clear→listeyi_temizler
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
meyveler.clear()
print(meyveler)
del meyveler
print(f"listemizin son hali → {meyveler}")
"""
# endregion

# region copy→listeyi_kopyalar
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"listemizin ilk hali → {meyveler}")
meyveTabagi = meyveler.copy()
print(f"listemizin son hali → {meyveTabagi}")
"""
# endregion

# region count→elaman_sayisi
"""
listeRakamlar = [2, 5, 6, 1, 9, 7, 5, 9]
arananEleman = 9
elemanAdedi = listeRakamlar.count(arananEleman)
print(f"listemizdeki {arananEleman} elemanı adedi→ {elemanAdedi}")
meyveler = ["elma", "armut", "muz", "ayva", "muz", "üzüm"]
print(meyveler.count("muzz"))
"""
# endregion

# region ornek_1
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"] 
arananMeyve = input("aramak istediğiniz meyve? : ")
elemanAdedi = meyveler.count(arananMeyve)
if elemanAdedi:   # elemanAdedi!=0
    print(f"aradığınız {arananMeyve} listede yer almaktadır.")
else:
    print(f"Aradığınız {arananMeyve} listede yer almamaktadır.")
"""
# endregion

# region sort_reverse→sirala_tersten_sirala
"""
listeRakamlar = [2, 5, 6, 1, 4, 9, 3, 8, 7]
print(f"listemizin ilk hali → {listeRakamlar}")
listeRakamlar.sort()
print(f"listemizin son hali → {listeRakamlar}")
listeRakamlar.reverse()
print(f"listemizin son hali → {listeRakamlar}")
"""
# endregion

# region index→arama_indeks_dondurme
"""
listeRakamlar = [2, 5, 6, 1, 9, 7]
print(listeRakamlar.index(10))
"""
# endregion