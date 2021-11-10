# region while-else
# WHILE döngüsü BREAK satırı ÇALIŞARAK biterse, else içerisine GİRMEZ
# WHILE döngüsü BREAK satırı ÇALIŞMADAN biterse, else içerisine GİRER
"""
i = 1
while i <= 10:
    print(i, end=" ")
    if i == 2:
        pass
        #break
    i += 1
else:
    print("şu an else içerisine girdim")
print("while döngüsü bitti")
"""
# endregion

# region for-else
# FOR döngüsü BREAK satırı ÇALIŞARAK biterse, else içerisine GİRMEZ
# FOR döngüsü BREAK satırı ÇALIŞMADAN biterse, else içerisine GİRER
"""
for i in range(10, 1, -1):
    print(i, end=" ")
    if i == 9:
        break
else:
    print("şu an for elsedeyim")
print("brdym")
"""
# endregion

searchId = -1
for orderId in range(1, 100000):
    if orderId == searchId:
        print(f"{searchId} nolu sipariş için detay listesi")
        print("...")
        break 
else:
    print(f"{searchId} nolu sipariş için kayıt bulunamadı")
