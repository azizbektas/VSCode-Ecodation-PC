#output anıdna casting - dönüşüm ile ilgili efor harcamamak için format yöntemleri kullanırız
#region format
#ekrana output formatlarken ilk yöntem → format
"""rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print("girdiğiniz rakamın bir fazlası {}".format(rakam+1))
print("girdiğiniz {} rakamının bir fazlası {}".format(rakam, (rakam+1)))"""
#endregion



#region fstring
#ekrana output formatlarken ilk yöntem → fstring
"""
rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print(f"girdiğiniz {rakam} rakamının bir fazlası {rakam+1}")
"""
s1 = int(input("l. s. g. : "))
s2 = int(input("l. s. g. : "))
print(f"girdiğiniz sayıların toplamı {s1+s2}")
print(f"{s1} + {s2} = {s1+s2}")
#endregion
#girdiğiniz sayıların toplamı 8
#3 + 5 = 8