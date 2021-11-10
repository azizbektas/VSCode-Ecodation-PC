#region nested_if
# iç içe döngü - iç içe loop
"""
i, j = 0, 0
while i<3:
    while j<3:
        print(f"{i} x {j}")
        j +=1
    i += 1
    j = 0
"""
#endregion

#region ornek_1
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *

i, j = 0, 0
while i<10:
    while j<10:
        print(" * ", end= "")
        j += 1
    i +=1
    j = 0
    print()
"""
#endregion

#region ornek_2
"""
i, j  = 0, 0
while i<10:
    while j<10:
        pass
"""         
#endregion