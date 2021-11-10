# region cok_boyutlu_listeler_giris
"""
matris yapıları oluşturma
veri tabanı mimarisine benzer satırxsütun yapıları oluşturma
"""
# endregion

# region kurum_ici_veri_tabani_ornegi
"""
Örn. kurum içi bilgisayarların özelliklerini tutacağınız bir tablo
Bil.No  Cihaz Adı       CPU     PID
1       Desktop_Test    %56     chrome.exe
2       Guest101        %60     excel.exe
3       Kat-1_Laptop    %90     camtasia.exe, chrome.exe
"""
# endregion

# region tanimlama
"""
1 2 3 4
5 6 7 8
ixj 2x4
a = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(a)
"""
# endregion

# region erisim
"""
a = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(a)
print(a[1])
print(a[0][2])
"""
# endregion

# region ornek
"""
kurumBilgisayarlari=[
    [1, "Kat1-PC", 45, "chrome.exe"], 
    [2, "Desktop-Lab1", 90, "chrome.exe, camtasia.exe"], 
    [3, "Misafir-PC", 25, "excel.exe"]
    ]
print(kurumBilgisayarlari)
print(kurumBilgisayarlari[2])
print(kurumBilgisayarlari[1][1])
if kurumBilgisayarlari[1][2]>80:
    print(kurumBilgisayarlari[1][3])
"""
# endregion

# region for_ile_erisim_1
"""
1 2 3 4
5 6 7 8

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for  i in range(len(a)):
    for j in range(len(a[i])):
        print(f"{a[i][j]}", end= " ")
    print()
"""
# endregion

# region for_ile_erisim_2
"""
kurumBilgisayarlari=[
    [1, "Kat1-PCCCC", 45, "chrome.exe"], 
    [2, "Desktop-Lab1", 84, "chrome.exe, camtasia.exe"], 
    [3, "Misafir-PC", 25, "excel.exe"]
    ]
print(f"satır sayısı → {len(kurumBilgisayarlari)}")
print(f"sütun sayısı → {len(kurumBilgisayarlari[0])}")


for i in range(len(kurumBilgisayarlari)):    #0,1,2
    for j in range(len(kurumBilgisayarlari[i])):
        print(f"{kurumBilgisayarlari[i][j]}\t", end="" )
    print()
"""
# endregion