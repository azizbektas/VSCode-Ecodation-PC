# region string_metodlari
"""
upper() lower() title() capatilize()
count() replace()   swapcase()
startswith()    endswith()
strip() lstrip()    rstrip()
isdigit()   isalpha()
isalphanum()    isspace()   istitle()   isidentifier()
split() index() find() format()
"""
# endregion

# region object
"""
#object
print(type(3))
kurum = "Ecodation Eğitim Kurumları"
yas = 34
"""
# endregion

# region upper
"""
büyük harfe çevirir
kurum = "Ecodation Eğitim Kurumları"
print(kurum.upper())
"""
# endregion

# region lower
"""
küçük harfe çevirir
kurum = "Ecodation Eğitim Kurumları"
print(kurum.lower())
while True:
    yas = input("yaş giriniz, çıkmak için ç ")
    if yas.lower()=="ç":
        break
"""
# endregion

# region title
"""
tüm kelimelerin yalnızca ilk harfleri büyük yazılır.
kurum = "ecodation eğitim kurumlarıııı"
print(kurum.title())
"""
# endregion

# region capitalize
"""
sadece ilk harf büyük, diğer tüm harfler küçük yazılır.
kurum = "Ecodation Eğitim Kurumları"
print(kurum.capitalize())
"""
# endregion

# region count
"""
parametrede belirttiğim harf, kelime neyse, string içinde kaç tane geçtiğini bulur.
kurum = "Ecodation Eğitim Kurumları"
print(kurum.count(("z")))
print(kurum.count("i", 6, 8))
"""
# endregion

# region replace
"""
bir metni, başka bir metin ile değiştirir.
url = "http://www.ecodation.com.tr"
url.replace("com.tr", "edu.tr")
print(url)
url = url.replace("com.tr", "edu.tr")
print(url)
yorum = "bu kelime sansürlenecek"
print(yorum.replace("sansürlenecek", "..."))
print(yorum)
"""
# endregion

# region swapcase
"""
Büyük karakterler küçük, küçük karakterler büyük olacak.
kurum  = "Ecodation Eğitim Kurumları"
print(kurum)
print(kurum.swapcase())
"""
# endregion

# region endswith
"""
endswith; eğer parametre ile belirttiğiniz haliyle bitiyorsa True, aksi takdirde False değeri döndürür.
url = "http://www.ecodation.com.tr"
print(url.endswith("com.tr"))
"""
# endregion

# region startswith
"""
startswith; eğer parametre ile belirttiğiniz haliyle başlıyorsa True, aksi takdirde False değeri döndürür.
url = "http://www.ecodation.com.tr"
print(url.startswith("http"))
print(url[0:4]=="http")
"""
# endregion

# region strip
"""
strip; ile başındaki sonundaki boşlukları almayı başaracağız.
kurum  = "        Ecodation Eğitim Kurumları         "
print(kurum)
print(kurum.strip())
"""
# endregion

# region lstrip
"""
lstrip; string değerin başındaki boşlukları alır.
kurum  = "        Ecodation Eğitim Kurumları"
print(kurum)
print(kurum.lstrip())
"""
# endregion

# region rstrip
"""
rstrip; string değerin sonundaki boşlukları alır.
kurum  = "Ecodation Eğitim Kurumları       "
print(kurum)
print(kurum.rstrip())
"""
# endregion

# region isdigit
"""
rakam olup/olmadığını geriye döndürür. Eğer değer bir sayı ise, tüm rakamlarını kontrol ederek 
True/False geriye döndürecek.

deger = "1"
print(deger.isdigit())
deger = "1060"
deger = "_1060"
print(deger.isdigit())
sayi = int(input("lütfen s. giriniz: "))
"""
# endregion

# region isalpha
"""
hepsi harf ise True, değilse False döner. Girilen değerlerin harf olup olmadığını sorgular.
deger = "nciSınıf"
print(deger.isalpha())
"""
# endregion

# region isalnum
"""
alfanumerik ise True, değilse False döner.
deger = "1nciSınıf"
print(deger.isalnum())
"""
# endregion

# region isupper
"""
tamamı büyük karakterlerden mi oluşuyor? 
kurum = "ECODATION"
print(kurum.isupper())
"""
# endregion

# region islower
"""
tamamı küçük karakterlerden mi oluşuyor? 
kurum = "ECODATIoN"
print(kurum.islower())
"""
# endregion

# region isspace
"""
tamamı space mi doğrulamak için kullanılır.
kurum = "     "
print(kurum.isspace())
"""
# endregion

# region istitle
"""
ilk harfleri büyük mü doğrulamak için kullanılır. 
deger = "Ecodation Eğitim kurumları"
print(deger.istitle())
"""
# endregion

# region isidentifier
"""
parametre ile belirtilen değer, değişken ismi olur mu olmaz mı doğrulamak için kullanılır.
deger = "_1Sayi"
print(deger.isidentifier())
"""
# endregion

# region split
"""
parametre ile belirtilen değer, değişken ismi olur mu olmaz mı doğrulamak için kullanılır.
kurum  = "Ecodation Eğitim Kurumları"
print(kurum.split())
kurum1  = "Ecodation Eğitim Kurumları. Python Kursuna Hoş Geldiniz"
print(kurum1.split("."))
cumleSayisi = len(kurum1.split("."))
print(cumleSayisi)
kurum  = "Ecodation Eğitim Kurumları. Python Kursuna Hoş Geldiniz"
listem = [i for i in kurum.split(".")]
print(listem)
"""
# endregion



# region index
"""
parametre ile belirtilen değeri, aramak için kullanılır. Bulamadığında hata fırlatır.
kurum  = "Ecodation Eğitim Kurumları"
print(kurum.index("Eğitim"))
print(kurum.index("eğitim"))
"""
# endregion

# region find
"""
parametre ile belirtilen değeri, aramak için kullanılır. Index'ten farkı bulamadığında -1 geriye döndürür
kurum  = "Ecodation Eğitim Kurumları"
print(kurum.find("Eğitim"))
print(kurum.find("eğitim"))
print(kurum[kurum.find("Eğitim"):])
"""
# endregion

# region ic_ice_kullanim
"""
kurum  = "Ecodation Eğitim Kurumları"
print(len(kurum.lower().upper().title().replace("ğ", "g")))
"""
# endregion

# region ornek
"""
kotuKelimeler = ["yuh", "tüh"]
yorum  = "Bu laptop'u geçtiğimiz aylarda aldım. Aldığıma bin pişmanım. Satıcıya yuh sana diyorum."
kelimeler =[i.rstrip(".") for i in yorum.split(" ")]
for item in kotuKelimeler:
    if item in kelimeler:
        yorum = yorum.replace(item, "...")
print(yorum)
"""
# endregion