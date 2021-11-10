# region siralama
# orjinal liste     9, 7, 5, 1, 3, 4, 2, 6, 8
# 1. Sıralamada     7, 5, 1, 3, 4, 2, 6, 8, 9
# 2. Sıralamada     5, 1, 3, 4, 2, 6, 7, 8, 9
# 3. Sıralamada     1, 3, 4, 2, 5, 6, 7, 8, 9
# ...
"""
"""
listem = [9, 7, 5, 1, 3, 4, 2, 6, 8]
while True:
    siraliMi = True
    for i in range(len(listem)-1):
        if listem[i]>listem[i+1]:
            listem[i], listem[i+1]= listem[i+1], listem[i]
            siraliMi = False
    if siraliMi:
        break
print(listem)
# endregion




# ödev →
"""
Lütfen Bir Sayı Giriniz: 183
Yüz Seksen Üç
"""


# ödev →
"""
ecodation
1 adet e
2 adet o
1 adet a
1 adet i
"""