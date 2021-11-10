# region for_giris
"""
for i in range(15):
    print(i, end= " ")
"""
# endregion

# region range
"""
sayiDizisi = list(range(15, 5, -1))
print(sayiDizisi)
"""

# endregion

# region ornek_1
"""
for i in range(1, 11): # 1 2 3 4 5 6 7 8 9 10
    if i !=5:
        print(f"{i}. Öğrenci")
"""
# endregion

# region ornek_2
"""
for i in range(1, 6):
    for j in range(1, 6):
        print(" * ", end= "")
    print()

[1 x 1 = 1]     [1 x 2 = 2]     [1 x 3 = 3]     [1 x 4 = 4]     [1 x 5 = 5]
[2 x 1 = 1]     [2 x 2 = 2]     [2 x 3 = 3]     [2 x 4 = 4]     [2 x 5 = 5]
[3 x 1 = 1]     [3 x 2 = 2]     [3 x 3 = 3]     [3 x 4 = 4]     [3 x 5 = 5]

for i in range(1, 6):
    for j in range(1, 6):
        print(f"[ {i}x{j} = {i*j} ]\t", end= "")
    print()
    """
# endregion  

# region pass
"""
for i in range(1,6):
    for j in range(1,6):
        pass
"""
# endregion 