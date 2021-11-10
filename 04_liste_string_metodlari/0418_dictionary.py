# region dictionary
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

3-) dictionary özellikleri
→ tek bir değişken adında birden fazla eleman saklama
→ en önemli özelliği indisli değildir, sıralı değildir
→ key-value pair dediğimiz çiftler halinde tanımlanır
→ duplicate eleman saklamaya izin vermemesi
→ eleman değerlerinin değiştirilebilir olması
→ tanımlama anında, aç kapa süslü parantez { } kullanılması
"""


# endregion

# region dictionary_tanimlama_erisim
"""
programlaDilleri = {
    "programlamaDili": "python",
    "seviye": "yüksek",
    "interpreter": True,
    "versiyon": 3.94
}
print(programlaDilleri)
print(programlaDilleri["seviye"])
print(programlaDilleri.keys())
print(programlaDilleri.values())
print(programlaDilleri.items())
"""
# endregion

# region dictionary_duplicate
"""
programlaDilleri ={
    "programlamaDili" : "python",
    "seviye" : "yüksek",
    "interpterer" : True,
    "version": 3.91,
    "programlamaDili" : "c#",
}
print(programlaDilleri)
"""
# endregion

# region dictionary_loop
"""
programaDilleri ={
    "programlamaDili" : "python",
    "seviye" : "yüksek",
    "interpterer" : True,
    "version": 3.91
}
for key, value in programaDilleri.items():
    print(key, value)
"""

# endregion

# region ornek_1
"""
trEn ={
    "kitap" : "book",
    "geliştirici" : "developer",
    "korsan" : "hacker",
    "information": "bilgi"
}

for key, value in trEn.items():
    print(f"{key} ifadesinin ingilizcesi → {value}")
"""
# endregion

# region ornek_2
"""
ipDetay = {
    "ip": {
        "query": "92.44.82.0",
        "status": "success",
        "continent": "Asia",
        "continentCode": "AS",
        "country": "Turkey",
        "countryCode": "TR",
        "region": "34",
        "regionName": "Istanbul",
        "city": "Istanbul",
        "district": "",
        "zip": "34110",
        "lat": 41.0205,
        "lon": 28.9753,
        "timezone": "Europe/Istanbul"
    },
    "dns": {
        "geo": "Turkey - Turkcell Internet"
    }
}
print(ipDetay["ip"]["lat"])
"""
# endregion

# region ornek_3
""""""
sirket = {
    "departman": {
        "yazılım": ["ali", "mehmet"],
        "muhasebe": ["inci", "elif"],
    },
    "calisanSayisi": 100,
    "ceo": "Ali Kemal",
    "telefonlar": {
        "istanbul": "021265656",
        "ankara": "031245656"
    },
    "sirketArabalari": ["i20", "renault megan", "ford focus"],
    "sirketArabalari2": {
        "i20": True,
        "renault megan": False,
        "ford focus": True
    }
}
print(sirket["calisanSayisi"])
print(sirket["ceo"])
print(sirket["departman"]["yazılım"])
print(sirket["departman"]["yazılım"][0])
print(sirket["sirketArabalari"][2])
print(sirket["sirketArabalari2"]["renault megan"])

# endregion


# ödev →
"""
lokasyon = {
   "info":{
      "statuscode":0,
      "copyright":{
         "text":"\u00A9 2021 MapQuest, Inc.",
         "imageUrl":"http://api.mqcdn.com/res/mqlogo.gif",
         "imageAltText":"\u00A9 2021 MapQuest, Inc."
      },
      "messages":[
         
      ]
   },
   "options":{
      "maxResults":-1,
      "thumbMaps":True,
      "ignoreLatLngInput":False
   },
   "results":[
      {
         "providedLocation":{
            "location":"istanbul"
         },
         "locations":[
            {
               "street":"",
               "adminArea6":"",
               "adminArea6Type":"Neighborhood",
               "adminArea5":"Istanbul",
               "adminArea5Type":"City",
               "adminArea4":"Fatih",
               "adminArea4Type":"County",
               "adminArea3":"\u0130STANBUL",
               "adminArea3Type":"State",
               "adminArea1":"TR",
               "adminArea1Type":"Country",
               "postalCode":"",
               "geocodeQualityCode":"A5XAX",
               "geocodeQuality":"CITY",
               "dragPoint":False,
               "sideOfStreet":"N",
               "linkId":"283510263",
               "unknownInput":"",
               "type":"s",
               "latLng":{
                  "lat":41.017058,
                  "lng":28.985568
               },
               "displayLatLng":{
                  "lat":41.017058,
                  "lng":28.985568
               },
               "mapUrl":"http://www.mapquestapi.com/staticmap/v5/map?key=eod44I9Nm3s0qCIGak31NZYQ9TloitnL&type=map&size=225,160&locations=41.017058,28.985568|marker-sm-50318A-1&scalebar=True&zoom=12&rand=-248896091"
            },
            {
               "street":"",
               "adminArea6":"",
               "adminArea6Type":"Neighborhood",
               "adminArea5":"",
               "adminArea5Type":"City",
               "adminArea4":"",
               "adminArea4Type":"County",
               "adminArea3":"\u0130STANBUL",
               "adminArea3Type":"State",
               "adminArea1":"TR",
               "adminArea1Type":"Country",
               "postalCode":"",
               "geocodeQualityCode":"A3XAX",
               "geocodeQuality":"STATE",
               "dragPoint":False,
               "sideOfStreet":"N",
               "linkId":"306019918",
               "unknownInput":"",
               "type":"s",
               "latLng":{
                  "lat":41.076602,
                  "lng":29.052495
               },
               "displayLatLng":{
                  "lat":41.076602,
                  "lng":29.052495
               },
               "mapUrl":"http://www.mapquestapi.com/staticmap/v5/map?key=eod44I9Nm3s0qCIGak31NZYQ9TloitnL&type=map&size=225,160&locations=41.076602,29.052495|marker-sm-50318A-2&scalebar=True&zoom=5&rand=-86489616"
            }
         ]
      }
   ]
}
"""