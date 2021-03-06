#derleme ile yorumlama
"""
compilation;
av
1-compile edilmiş kodların, execute işlemi hızlıdır
2-compiler sadece kod yazılan pc de olması yeter, son kullanıcıda olmasına gerek yok
3-compile edilen kodlar makine diline çevirileceği için son kullanıcının bu kodları anlaması zordur, 
kodların manipulasyonları o yüzden zordur, (tam olarak katılamacağım)

dez
1-compile işlemi, derleme işlemi anı yavaştır, ilk anda uzun sürebilir.
2-compiler, donanım platformuna göre farklılık gösterir, platform bağımlıdır özetle
-------
interpretation
av
1-kodu yazar ve çalıştırırsınız, ek derleme süresi istemez
2-platform bağımlı değildir, her donanımda, her işletim sisteminde çalışır, ayrı ayrı derleyiciler istemez, 
tek ihtiyaç duyduğu runtime da iken yani çalışma anında interpreter olsun bitti gitti, 
o da python kütüphanelerinde var zaten

dez
1-tüm kaynağı run-time da iken tüketir, çalışma anı yavaştır
2-hem kodu yazan kişi olarak siz, hem de son kullanıcının bilgisayarında interpreter olmalı
"""