# region kargs_giris
"""
Argüman olarak → int, float, string, list gönderebiliyorum, peki
Argüman olarak → dictionary gönderebilir miyim? Cevabı, Evet
"""
# endregion

# region ornek_1
"""
def pDilleri(**kargs):
    print(type(kargs))
    for key, value in kargs.items():
        print(f"{key} {value}")

pDilleri(
    programlamaDili="python",
    seviye="yüksek",
    interpreter=True,
    veryison=3.64
)
"""
# endregion

# region ornek_2
"""

dilPython = {
    "programlamaDili" : "python",
    "seviye" : "yüksek",
    "interpreter" : True,
    "versiyon" : 3.64
}

dilCSharp = {
    "programlamaDili" : "c#",
    "seviye" : "yüksek",
    "interpreter": False,
    "versiyon" : 8.0
}

def dilBilgisi(dil):
    print(f"{dil['programlamaDili']}\t{dil['seviye']}\t{dil['interpreter']}\t{dil['versiyon']}")


print("Prg.Dil\tSeviye\tInterp\tVersiyon")
print("-------\t-------\t-------\t-------")

dilBilgisi(dilPython)
dilBilgisi(dilCSharp)
"""
# endregion

# region ornek_3
""""""
diller = {
    "dilPython" : {
        "programlamaDili": "python",
        "seviye": "yüksek",
        "interpreter": True,
        "versiyon": 3.64
    },

    "dilCSharp" : {
        "programlamaDili": "c#",
        "seviye": "yüksek",
        "interpreter": False,
        "versiyon": 8.0
    }
}


def dilBilgisi(dil):
    for key in dil.keys():
        print(f"{dil[key]['programlamaDili']}\t{dil[key]['seviye']}\t{dil[key]['interpreter']}\t{dil[key]['versiyon']}")
        #print(key)

print("Prg.Dil\tSev.\tInterp.\tVersiyon")
print("------\t------\t------\t------")
dilBilgisi(diller)

# endregion