# region tuples_tiyuples
"""
1→ list
2→ tuple
3→ dictionary

1-) list özellikleri
→ tek bir değişken adında birden fazla eleman saklama
→ sıralı index özelliği
→ zero based’dir. İlk eleman [0], ikinci eleman [1]
→ duplicate eleman saklamaya izin vermesi
→ eleman değerlerinin değiştirilebilmesi
→ tanımlama anında, köşeli parantez [ ] kullanılması


2-) tuple özellikleri
→ tek bir değişken adında birden fazla eleman saklama
→ sıralı index özelliği. 
→ zero based’dir. İlk eleman [0], ikinci eleman [1]
→ duplicate eleman saklamaya izin vermesi
→ eleman değerlerinin değiştirilememesi
→ tanımlama anında, aç kapa parantez ( ) kullanılması
"""
# endregion

# region tuple_tanimlama_erisim
"""
tupleListem = (3, 5, 6, 2, 9, 7, 3.14)
print(tupleListem)
rakamlar = 3, 5, 6
print(rakamlar)
print(tupleListem[2])
"""
# endregion

# region tuple_guncelleme
"""
tupleListem = (1, 2, 4, 8, 2, 3.14)
tupleListem[0] = "sıfır"
"""
# endregion

# region tuple vs list
"""
                                    tuple   list
1→  birden fazla veri depolama      +       +
2→  farklı tipte veri depolama      +       +
3→  iterable/indeksli               +       +
4→  ekleme/çıkarma                  -       +
5→  arama                           +       -
6→  debugging                       +       -
7→  hafıza kullanımı                -       +
"""
# endregion

# region tuple_loop
"""
tupleListem = (1, 2, 4, 8, 2, 3.14)
print([i for i in tupleListem if i>=4])
tupleListem = (1, 2, 4, 8, 2, 3.14)
listem= []
for i in tupleListem:
    if i>=4:
        listem.append(i)
print(listem)
"""
# endregion

# region tuple_metodlari_index
"""
tupleListem = (1, 2, 4, 8, 2, 3.14)
x = input("Aradığınız Eleman : ")
if x.isdigit():
    x = int(x)
    if x in tupleListem:
        print(f"aradığınız {x} değeri {tupleListem.index(x)+1}. indekslidir")
    else:
        print(f"aradığınız {x} değeri listede yoktur")
else:
    print("lütfen sayısal değer giriniz")
"""
# endregion

# region tuple_slice
"""
tupleListem = (1, 2, 4, 8, 2, 3.14)
print(tupleListem[:])
print(tupleListem[-1])
print(tupleListem[1:4])
print(tupleListem[1:])
"""
# endregion

# region tuple_join
"""
tupleAdayListe1 = (1, 2, 3, 6, 8)
tupleAdayListe2 = (10, 15)
tupleAsilListe = tupleAdayListe1 + tupleAdayListe2
print([i for i in tupleAsilListe])
listem = [i for i in tupleAsilListe]
print(f"ortalaması {sum(listem)/len(listem)}")
print(f"minimum değer {min(listem)}")
print(tupleAsilListe)
"""
# endregion